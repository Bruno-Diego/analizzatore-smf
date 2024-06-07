from datetime import datetime, timedelta
from decimal import Decimal
from typing import Dict, List

from data_layer.machine_states import Machine_states
from data_layer.record_smf import Record_smf
from utils.messages import Messages


class Estrattore(object):
    """
    # Estrattore
    
    Estrattore dei record SMF con pulizia dei campi e delle righe
    non utili per l'analisi
    """
    def __init__(self, 
        p_file_name: str,
        p_messages : Messages,
    ):
        """
        # Estrattore
        
        Estrattore dei record SMF con pulizia dei campi e delle righe
        non utili per l'analisi
        """
        super().__init__()
        
        self.file_name = p_file_name
        self.msgs = p_messages
        self.lista_records: List[Record_smf] = []
        self.righe_file: List[str] = []
        
        # self.load_testo()
        # self.interpreta_righe()


    def load_testo(self):
        """
        # load_testo
        
        Leggo il file, pulendo i caratteri e carica una lista di stringhe
        corrispondenti alle righe del file.
        """
        # Leggo il file in modalità binaria per caricare
        # anche i caratteri "strani" che arrivano dal mainframe
        # with open(self.file_name, 'rb') as fil:
        #     byte_arr = fil.read()
            
        # in questo caso lo file viene aperto
        byte_arr = self.file_name.read()
        
        # Considero il testo come ASCII per eliminare tutti i caratteri "strani"
        # che poi UTF-8 non capisce
        str_ascii = byte_arr.decode(encoding='ascii', errors='replace')
        
        # Elimino tutti i caratteri oltre il 128. Uso ASCII 7 bit completo
        str_ascii = ''.join(
            [
                i if ord(i) < 127 and ord(i) != 0 and ord(i) != 12 and ord(i) != 15
                else ' ' 
                for i in str_ascii
            ]
        )
        
        self.righe_file = str_ascii.split("\r\n")       
       
        # Scarica il riferimento per consentire la garbage collection
        # immediata
        byte_arr  = []
        str_ascii = []

        # for _row in self.righe_file: 
        #     print(f'§§ {_row} §§')


    def interpreta_righe(self) -> str:
        """
        # interpreta_righe
        
        Legge l'array con le righe caricate in memoria
        e esegue il parsing in una lista di records dei 
        campi della SMF 123 Subtype 2

        ## Ritorna:
            str: OK, oppure un messaggio di errore.
        """
        _ret_val = 'OK'      
        _enumst = Machine_states()
        _stato = _enumst.INITIAL
        
        _smf_123_is_found = False
        _smf_ssi_is_ZCON = False
        _smf_subtype_is_2 = False
        _smf_subtype_version_is_2 = False
        
        _idx = 0
        
        try:
        
            for _idx, _row in enumerate(self.righe_file):
                
                # STATO INITIAL: Rimango nello stato e leggo la linea successiva 
                # Finché non trovo la rottura e passo allo stato HEADER_EXTENSION
                if _stato == _enumst.INITIAL:
                    if _row.find('* SMF Record Header *') != -1:
                        _rec = Record_smf()
                        _stato = _enumst.RECORD_HEADER
                elif _stato == _enumst.RECORD_HEADER:
                    # Verifica che il file sia effettivamente SMF123
                    if (_val := self.estrai_campo('SMF123_REC_TYPE', _row)) is not None:
                        if _val.upper() != '123':
                            return self.msgs.SMFF_0001_RECORD_SMF_NO_123(
                                'Estrattore',
                                'interpreta_righe',
                                self.file_name,
                                'REC_TYPE',
                                '123'
                            )
                        else:
                            _smf_123_is_found = True
                    if (_val := self.estrai_campo('SMF123_SSI', _row)) is not None:
                        if _val.upper() != 'ZCON': 
                            return self.msgs.SMFF_0001_RECORD_SMF_NO_123(
                                'Estrattore',
                                'interpreta_righe',
                                self.file_name,
                                'SMF123_SSI',
                                'ZCON'
                            )
                        else:
                            _smf_ssi_is_ZCON = True
                    if (_val := self.estrai_campo('SMF123_SUBTYPE', _row)) is not None:
                        if _val.upper() != '2':
                            # MV : 2024-05-22 13:47:14 - Salto il record se non è
                            # un SMF123 SUBTYPE 2: così nei file "mixed" (Che sono sovente 
                            # presenti)
                            print( self.msgs.SMFF_0001_RECORD_SMF_NO_123(
                                'Estrattore',
                                'interpreta_righe',
                                self.file_name,
                                'SMF123_SUBTYPE',
                                '2'
                            ))
                            _stato = _enumst.INITIAL
                            continue
                        else:
                            _smf_subtype_is_2 = True
                    if (_val := self.estrai_campo('SMF123S2_SUBTYPE_VERSION', _row)) is not None:
                        if _val.upper() != '2':
                            return self.msgs.SMFF_0001_RECORD_SMF_NO_123(
                                'Estrattore',
                                'interpreta_righe',
                                self.file_name,
                                'SMF123S2_SUBTYPE_VERSION',
                                '2'
                            )
                        else:
                            _smf_subtype_version_is_2 = True
                    if (_val := self.estrai_campo('SMF123_SID', _row)) is not None:
                        _rec.SMF123_SID = _val
                    elif _row.find('* SMF123.2 V2 Header Extension *') != -1:
                        _stato = _enumst.HEADER_EXTENSION
                        
                elif _stato == _enumst.HEADER_EXTENSION:
                    # Verifica che i "fingerprint" per essere un SMF 123 Subtype 2 
                    # siano ok
                    
                    _manca_header = ''
                    if not _smf_123_is_found: 
                        _manca_header = 'SMF123_REC_TYPE'
                    if not _smf_ssi_is_ZCON: 
                        _manca_header += _manca_header + ', SMF123_SSI'
                    if not _smf_subtype_is_2:
                        _manca_header += _manca_header + ', SMF123_SUBTYPE'
                    if not _smf_subtype_version_is_2:
                        _manca_header += _manca_header + ', SMF123S2_SUBTYPE_VERSION'
                    if _manca_header != '':
                        return self.msgs.SMFF_0002_HEADERS_MANCANTI(
                            'Estrattore',
                            'interpreta_righe',
                            self.file_name,
                            _manca_header
                        )
                    
                    # Le header extensions vengono saltate
                    if _row.find('* SMF123.2 V2 Server Section *') != -1:
                        _stato = _enumst.SERVER_SECTION
                        
                elif _stato == _enumst.SERVER_SECTION:
                    if   (_val := self.estrai_campo('SMF123_SERVER_SECT_VERSION', _row)) is not None:
                        _rec.SMF123_SERVER_SECT_VERSION = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_SYSTEM', _row)) is not None:
                        _rec.SMF123_SERVER_SYSTEM = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_SYSPLEX', _row)) is not None:
                        _rec.SMF123_SERVER_SYSPLEX = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_JOBID', _row)) is not None:
                        _rec.SMF123_SERVER_JOBID = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_JOBNAME', _row)) is not None:
                        _rec.SMF123_SERVER_JOBNAME = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_STOKEN', _row)) is not None:
                        _rec.SMF123_SERVER_STOKEN = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_CONFIG_DIR', _row)) is not None:
                        _rec.SMF123_SERVER_CONFIG_DIR = _val
                    elif (_val := self.estrai_campo('SMF123_SERVER_VERSION', _row)) is not None:
                        _rec.SMF123_SERVER_VERSION = _val
                    elif _row.find('* SMF123.2 V2 Request Data Section *') != -1:
                        _stato = _enumst.REQUEST_DATA_SECTION

                elif _stato == _enumst.REQUEST_DATA_SECTION:
                    if   (_val := self.estrai_campo('SMF123S2_REQ_DATA_VERSION', _row)) is not None:
                        _rec.SMF123S2_REQ_DATA_VERSION = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_APP_TYPE', _row)) is not None:
                        _rec.SMF123S2_REQ_APP_TYPE = _val
                    elif (_val := self.estrai_campo('SMF123S2_HTTP_RESP_CODE', _row)) is not None:
                        _rec.SMF123S2_HTTP_RESP_CODE = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_STATUS_CODE', _row)) is not None:
                        _rec.SMF123S2_REQ_STATUS_CODE = _val
                    elif (_val := self.estrai_campo('SMF123S2_RESP_FLAGS', _row)) is not None:
                        _rec.SMF123S2_RESP_FLAGS = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_RETRIED', _row)) is not None:
                        _rec.SMF123S2_REQ_RETRIED = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_PAYLOAD_LEN', _row)) is not None:
                        _rec.SMF123S2_REQ_PAYLOAD_LEN = _val
                    elif (_val := self.estrai_campo('SMF123S2_RESP_PAYLOAD_LEN', _row)) is not None:
                        _rec.SMF123S2_RESP_PAYLOAD_LEN = _val
                    elif (_val := self.estrai_campo('SMF123S2_USER_NAME_MAPPED', _row)) is not None:
                        _rec.SMF123S2_USER_NAME_MAPPED = _val
                    elif (_val := self.estrai_campo('SMF123S2_USER_NAME_ASSERTED', _row)) is not None:
                        _rec.SMF123S2_USER_NAME_ASSERTED = _val
                    elif (_val := self.estrai_campo('SMF123S2_API_REQ_NAME', _row)) is not None:
                        _rec.SMF123S2_API_REQ_NAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_API_REQ_VERSION', _row)) is not None:
                        _rec.SMF123S2_API_REQ_VERSION = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_REFERENCE', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_REFERENCE = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_HOST', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_HOST = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_PORT', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_PORT = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_FULL_PATH', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_FULL_PATH = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_METHOD', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_METHOD = _val
                    elif (_val := self.estrai_campo('SMF123S2_ENDPOINT_QUERY_STR', _row)) is not None:
                        _rec.SMF123S2_ENDPOINT_QUERY_STR = _val
                    elif (_val := self.estrai_campo('SMF123S2_TIME_STUB_SENT', _row)) is not None:
                        _rec.SMF123S2_TIME_STUB_SENT = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_STUB_SENT', _row)) is not None:
                        # _rec.UTC_CONV_TIME_STUB_SENT = self.converti_tempi_con_null(_val)
                        _rec.UTC_CONV_TIME_STUB_SENT = _val
                    elif (_val := self.estrai_campo('SMF123S2_TIME_ZC_ENTRY', _row)) is not None:
                        _rec.SMF123S2_TIME_ZC_ENTRY = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_ZC_ENTRY', _row)) is not None:
                        # _rec.UTC_CONV_TIME_ZC_ENTRY = self.converti_tempi_con_null(_val)
                        _rec.UTC_CONV_TIME_ZC_ENTRY = _val
                    elif (_val := self.estrai_campo('SMF123S2_TIME_ZC_EXIT', _row)) is not None:
                        _rec.SMF123S2_TIME_ZC_EXIT = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_ZC_EXIT', _row)) is not None:
                        # _rec.UTC_CONV_TIME_ZC_EXIT = self.converti_tempi_con_null(_val)
                        _rec.UTC_CONV_TIME_ZC_EXIT = _val
                    elif (_val := self.estrai_campo('SMF123S2_TIME_TOKEN_GET_START', _row)) is not None:
                        _rec.SMF123S2_TIME_TOKEN_GET_START = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_TOKEN_GET_START', _row)) is not None:
                        _rec.UTC_CONV_TIME_TOKEN_GET_START = self.converti_tempi_con_null(_val)
                    elif (_val := self.estrai_campo('SMF123S2_TIME_TOKEN_GET_FINISH', _row)) is not None:
                        _rec.SMF123S2_TIME_TOKEN_GET_FINISH = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_TOKEN_GET_FINISH', _row)) is not None:
                        _rec.UTC_CONV_TIME_TOKEN_GET_FINISH = self.converti_tempi_con_null(_val)
                    elif (_val := self.estrai_campo('SMF123S2_TIME_ENDPOINT_SENT', _row)) is not None:
                        _rec.SMF123S2_TIME_ENDPOINT_SENT = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_ENDPOINT_SENT', _row)) is not None:
                        # _rec.UTC_CONV_TIME_ENDPOINT_SENT = self.converti_tempi_con_null(_val)
                        _rec.UTC_CONV_TIME_ENDPOINT_SENT = _val
                    elif (_val := self.estrai_campo('SMF123S2_TIME_ENDPOINT_RECEIVED', _row)) is not None:
                        _rec.SMF123S2_TIME_ENDPOINT_RECEIVED = _val
                    elif (_val := self.estrai_campo('UTC_CONV_TIME_ENDPOINT_RECEIVED', _row)) is not None:
                        # _rec.UTC_CONV_TIME_ENDPOINT_RECEIVED = self.converti_tempi_con_null(_val)
                        _rec.UTC_CONV_TIME_ENDPOINT_RECEIVED = _val
                    elif (_val := self.estrai_campo('SMF123S2_MVS_JOBNAME', _row)) is not None:
                        _rec.SMF123S2_MVS_JOBNAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_MVS_JOBID', _row)) is not None:
                        _rec.SMF123S2_MVS_JOBID = _val
                    elif (_val := self.estrai_campo('SMF123S2_MVS_SYSNAME', _row)) is not None:
                        _rec.SMF123S2_MVS_SYSNAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_MVS_ASID', _row)) is not None:
                        _rec.SMF123S2_MVS_ASID = _val
                    elif (_val := self.estrai_campo('SMF123S2_MVS_SID', _row)) is not None:
                        _rec.SMF123S2_MVS_SID = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_APPLID', _row)) is not None:
                        _rec.SMF123S2_CICS_APPLID = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_TASK_NUMBER', _row)) is not None:
                        _rec.SMF123S2_CICS_TASK_NUMBER = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_TRANSID', _row)) is not None:
                        _rec.SMF123S2_CICS_TRANSID = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_RMUOWID', _row)) is not None:
                        _rec.SMF123S2_CICS_RMUOWID = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_NETUOW_PX', _row)) is not None:
                        _rec.SMF123S2_CICS_NETUOW_PX = _val
                    elif (_val := self.estrai_campo('SMF123S2_CICS_NETUOW_SX', _row)) is not None:
                        _rec.SMF123S2_CICS_NETUOW_SX = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_IDENTIFIER', _row)) is not None:
                        _rec.SMF123S2_IMS_IDENTIFIER = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_REGION_ID', _row)) is not None:
                        _rec.SMF123S2_IMS_REGION_ID = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_TRANSNAME', _row)) is not None:
                        _rec.SMF123S2_IMS_TRANSNAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_APPNAME', _row)) is not None:
                        _rec.SMF123S2_IMS_APPNAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_PSBNAME', _row)) is not None:
                        _rec.SMF123S2_IMS_PSBNAME = _val
                    elif (_val := self.estrai_campo('SMF123S2_IMS_RECOVERY_TOKEN', _row)) is not None:
                        _rec.SMF123S2_IMS_RECOVERY_TOKEN = _val                    
                    elif (_val := self.estrai_campo('SMF123S2_REQ_ID', _row)) is not None:
                        _rec.SMF123S2_REQ_ID = _val                   
                    elif (_val := self.estrai_campo('SMF123S2_TRACKING_TOKEN', _row)) is not None:
                        # Il tracking Token, va su due righe: attivo uno stato
                        # tracking token e poi risalto qui
                        _token_part_1 = _val
                        _stato = _enumst.TRACKING_TOKEN
                    elif (_val := self.estrai_campo('SMF123S2_REQ_HDR1', _row)) is not None:
                        _rec.SMF123S2_REQ_HDR1 = _val                   
                    elif (_val := self.estrai_campo('SMF123S2_REQ_HDR2', _row)) is not None:
                        _rec.SMF123S2_REQ_HDR2 = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_HDR3', _row)) is not None:
                        _rec.SMF123S2_REQ_HDR3 = _val
                    elif (_val := self.estrai_campo('SMF123S2_REQ_HDR4', _row)) is not None:
                        _rec.SMF123S2_REQ_HDR4 = _val                    
                    elif (_val := self.estrai_campo('SMF123S2_RESP_HDR1', _row)) is not None:
                        _rec.SMF123S2_RESP_HDR1 = _val                   
                    elif (_val := self.estrai_campo('SMF123S2_RESP_HDR2', _row)) is not None:
                        _rec.SMF123S2_RESP_HDR2 = _val
                    elif (_val := self.estrai_campo('SMF123S2_RESP_HDR3', _row)) is not None:
                        _rec.SMF123S2_RESP_HDR3 = _val
                    elif (_val := self.estrai_campo('SMF123S2_RESP_HDR4', _row)) is not None:
                        _rec.SMF123S2_REQ_HDR4 = _val                       
                    elif _row.find('* SMF123.2 V2 Request Data Section *') != -1 \
                        or _idx >= len(self.righe_file) -1 :
                        ## NOTA: la verifica della riga finale '---------' non funziona 
                        ##       perché la riga compare altre 750 volte per cui aggiunge campi 
                        ##       vuoti. Quindi si verifica se ho finito le righe.

                        # Campi Calcolati
                        
                        _utc_conv_time_zc_entry_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_ZC_ENTRY)
                        _utc_conv_time_stub_sent_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_STUB_SENT)
                        _delta = _utc_conv_time_zc_entry_date - _utc_conv_time_stub_sent_date
                        _rec.ELAPSED_ZC_ENTRY_TO_STUB = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _utc_conv_time_endpoint_sent_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_ENDPOINT_SENT)
                        _delta = _utc_conv_time_endpoint_sent_date - _utc_conv_time_zc_entry_date
                        _rec.ELAPSED_ENDPOINT_SENT_ZC_ENTRY = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _utc_conv_time_endpoint_received_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_ENDPOINT_RECEIVED)
                        _delta = _utc_conv_time_endpoint_received_date - _utc_conv_time_endpoint_sent_date
                        _rec.ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _utc_conv_time_zc_exit_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_ZC_EXIT)
                        _delta = _utc_conv_time_zc_exit_date - _utc_conv_time_endpoint_received_date
                        _rec.ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _utc_conv_time_zc_exit_date = self.converti_tempi_con_null(_rec.UTC_CONV_TIME_ZC_EXIT)
                        _delta = _utc_conv_time_zc_exit_date - _utc_conv_time_zc_entry_date
                        _rec.ELAPSED_ZC_AND_ENDPOINT = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _delta = _utc_conv_time_zc_exit_date - _utc_conv_time_stub_sent_date
                        _rec.ELAPSED_TOTAL = Decimal(_delta.total_seconds()).quantize(Decimal('1.000000'))
                        
                        _rec.CLONE = _rec.SMF123S2_MVS_JOBNAME[0:2]
                        
                        
                        _old_rec = _rec
                        self.lista_records.append(_rec)
                        _rec = Record_smf()
                        _rec.carica_parte_fissa(
                            _old_rec.SMF123_SID,
                            _old_rec.SMF123_SERVER_SYSTEM,
                            _old_rec.SMF123_SERVER_SYSPLEX,
                            _old_rec.SMF123_SERVER_JOBID,
                            _old_rec.SMF123_SERVER_JOBNAME,
                            _old_rec.SMF123_SERVER_STOKEN,
                            _old_rec.SMF123_SERVER_CONFIG_DIR,
                            _old_rec.SMF123_SERVER_VERSION,
                        )

                elif _stato == _enumst.TRACKING_TOKEN:
                    _rec.SMF123S2_TRACKING_TOKEN = _val + _row.strip()
                    _stato = _enumst.REQUEST_DATA_SECTION

                # if _idx == 23:
                #     1/0
                    
            return 'OK'   

        except Exception as ex:
            print(f"\n\nERRORE ANALISI LINEA : {_idx + 1} : {str(ex)}")
            # raise ex
            
                    
    def converti_tempi_con_null(self, 
        p_tempo: str,
    ) -> datetime:
        if p_tempo == '' or p_tempo == '0000/00/00 00:00:00.000000':
            return None
        else:
            return datetime.strptime(p_tempo, '%Y/%m/%d %H:%M:%S.%f %Z')   
                    
    def estrai_campo(self,
        p_campo: str, 
        p_riga: str
    ) -> str:
        """
        # estrai_campo
        
        Estrae il campo dalla riga passata. Il campo deve essere del 
        tipo Nome_campo = valore il risultato è None se non ho trovato 
        il campo nella riga.
        
        ## Parametri posizionali
        
        - p_campo : nome del campo da ricercare all'interno della riga
        - p_riga : riga di testo dove cercare il campo
        
        ## Output
        
        La funzione ritorna None se il campo non è presente nella riga
        altrimenti ritorna il valore del campo a destra dell'= della 
        riga.
        """
        if p_riga.find('=') == -1:
            return None
        
        _splitarr = p_riga.split('=')
        
        if len(_splitarr) != 2:
            return None
        
        _left = _splitarr[0].strip()
        _right = _splitarr[1].strip()
        
        if _left == p_campo:
            return _right
        else:
            return None

if __name__ == '__main__':    
    
    _msg = Messages()
    _est = Estrattore('ZOSSMF123', Messages)
    _est.load_testo()
    _est.interpreta_righe()
    _max_row = 10 
    # _max_row = -1   # Se scrivo -1 arriva fino in fondo
    _idx = 0
    for _idx, _rec in enumerate(_est.lista_records):
        print()
        print(f'------- ROW {_idx} --------')
        print(f'SMF123_SERVER_JOBID: {_rec.SMF123_SERVER_JOBID}')
        print(f'SMF123S2_API_REQ_NAME: {_rec.SMF123S2_API_REQ_NAME}')
        print(f'SMF123S2_ENDPOINT_REFERENCE: {_rec.SMF123S2_ENDPOINT_REFERENCE}')
        print(f'SMF123S2_ENDPOINT_HOST: {_rec.SMF123S2_ENDPOINT_HOST}')
        print(f'SMF123S2_ENDPOINT_METHOD: {_rec.SMF123S2_ENDPOINT_METHOD}')
        print(f'UTC_CONV_TIME_STUB_SENT: {_rec.UTC_CONV_TIME_STUB_SENT}')
        print(f'UTC_CONV_TIME_ZC_ENTRY: {_rec.UTC_CONV_TIME_ZC_ENTRY}')
        print(f'ELAPSED_ZCENTRY_TO_STUB: {_rec.ELAPSED_ZC_ENTRY_TO_STUB}')
        print(f'UTC_CONV_TIME_ENDPOINT_SENT: {_rec.UTC_CONV_TIME_ENDPOINT_SENT}')
        print(f'ELAPSED_ENDPOINT_SENT_ZC_ENTRY: {_rec.ELAPSED_ENDPOINT_SENT_ZC_ENTRY}')
        print(f'UTC_CONV_TIME_ENDPOINT_RECEIVED: {_rec.UTC_CONV_TIME_ENDPOINT_RECEIVED}')
        print(f'ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT: {_rec.ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT}')
        print(f'UTC_CONV_TIME_ZC_EXIT: {_rec.UTC_CONV_TIME_ZC_EXIT}')
        print(f'ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED: {_rec.ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED}')
        print(f'ELAPSED_ZC_AND_ENDPOINT: {_rec.ELAPSED_ZC_AND_ENDPOINT}')
        print(f'ELAPSED_TOTAL: {_rec.ELAPSED_TOTAL}')
        print(f'SMF123S2_MVS_JOBNAME: {_rec.SMF123S2_MVS_JOBNAME}')
        print(f'SMF123S2_MVS_JOBID: {_rec.SMF123S2_MVS_JOBID}')
        print(f'SMF123S2_CICS_APPLID: {_rec.SMF123S2_CICS_APPLID}')
        print(f'SMF123S2_CICS_TASK_NUMBER: {_rec.SMF123S2_CICS_TASK_NUMBER}')
        print(f'SMF123S2_CICS_TRANSID: {_rec.SMF123S2_CICS_TRANSID}')
        
        if _idx == _max_row:
            break
    print()
    print()
    print('-' *30)
    print(f'Total Records : {len(_est.lista_records)}')
    print('-' *30)

    # print(_est.load_testo.__doc__)