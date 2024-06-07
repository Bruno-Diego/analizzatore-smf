from datetime import datetime
from decimal import Decimal
from typing import Dict


class Record_smf(object):
    """
    # Record_smf
    
    Classe che rappresenta un record SMF 123 Type 2. I commenti sono 
    descrittivi del contentunto dei vari campi (se conosciuto)
    
    ## ATTENZIONE
    
    Per questi campi è possibile che se non sono valorizzati, non siano 
    presenti. Quindi l'estrattore deve comunque verificare la loro presenza
    ed eventualmente caricarli se presenti.
    """
    def __init__(self, 
    ):    
        """
        # Record_smf
        
        Classe che rappresenta un record SMF 123 type 2. I commenti sono 
        descrittivi del contentunto dei vari campi (se conosciuto)
        """
        super().__init__()

        
        self.help_list: Dict[str, str] = {}
        """
        Dizionario per l'help degli attributi che corrispondono
        ai campi del SMF 123 Type 2 ed ai campi calcolati
        """

        ### NOTE (valid for all other fields also)
        ### in theory, the following should 
        ### be self.help_list['TRAN'] = self.TRAN.__doc__
        ### But by doing this, you will receive the help for 
        ### the value, not the help for the fields, i.e. 
        ### for a definition of
        ### self.TRAN = ''
        ### """
        ### Transaction identification.
        ### """
        ### self.TRAN.__doc__ will list the documentation for
        ### the string, not the 

        

        #### SMF RECORD HEADER, UNO SOLO PER FILE

        ### I CAMPI: 
        #           SMF123_REC_TYPE = 123
        #        
        #           SMF123_SSI = ZCON
        #           SMF123_SUBTYPE = 2
        #           SMF123S2_SUBTYPE_VERSION = 2
        # Possono essere usati per identificare il file e dare errore se non è un file SMF 123 subtype 2

        # self.SMF123_TIME = datetime.min
        self.SMF123_TIME = ''
        """
        Time when record was moved into the SMF buffer, in hundredths of a second since midnight.
        """
        self.help_list['SMF123_TIME'] = """
        Time when record was moved into the SMF buffer, in hundredths of a second since midnight.
        """

        #### HEADER EXTENSION 
        #    SMF123S2_TRIPLET_COUNT = 2
        #    SMF123S2_TRIPLET_OFFSET = 40
        #    SMF123S2_DATETIME_OFFSET = 0x00001AD2 74800000
        #    SMF123S2_SERVER_OFFSET = 56
        #    SMF123S2_SERVER_LEN = 188
        #    SMF123S2_SERVER_COUNT = 1
        #    SMF123S2_REQ_DATA_OFFSET = 244
        #    SMF123S2_REQ_DATA_LEN = 1560
        #    SMF123S2_REQ_DATA_COUNT = 20
        ## Questo non è necessario tutto, sembrano dati per il formato binario

        # self.SMF123_DATE = datetime.min
        self.SMF123_DATE = ''
        """
        Date when record was moved into the SMF buffer, YY is the current year (0 -99), DDD is the current day (1 -366), and F is the sign.
        """
        self.help_list['SMF123_DATE'] = """
        Date when record was moved into the SMF buffer, YY is the current year (0 -99), DDD is the current day (1 -366), and F is the sign.
        """


        self.SMF123_SID = ''
        """
        System ID from the SID parameter.
        """
        self.help_list['SMF123_SID'] = """
        System ID from the SID parameter.
        """


        self.SMF123_SERVER_SECT_VERSION = 0
        """
        Version of the server section.
        """
        self.help_list['SMF123_SERVER_SECT_VERSION'] = """
        Version of the server section.
        """

                
        self.SMF123_SERVER_SYSTEM = ''
        """
        System name (CVTSNAME).
        """
        self.help_list['SMF123_SERVER_SYSTEM'] = """
        System name (CVTSNAME).
        """
        
        
        self.SMF123_SERVER_SYSPLEX = ''
        """
        Sysplex name (ECVTSPLX).
        """
        self.help_list['SMF123_SERVER_SYSPLEX'] = """
        Sysplex name (ECVTSPLX).
        """
        
        
        self.SMF123_SERVER_JOBID = ''
        """
        Job ID of the server (JSABJBID).
        """
        self.help_list['SMF123_SERVER_JOBID'] = """
        Job ID of the server (JSABJBID).
        """
        
        
        self.SMF123_SERVER_JOBNAME = ''
        """
        Job name of the server (JSABJBNM).
        """
        self.help_list['SMF123_SERVER_JOBNAME'] = """
        Job name of the server (JSABJBNM).
        """
        
        
        self.SMF123_SERVER_STOKEN = ''
        """
        SToken of the server (ASS-BSTKN).
        """
        self.help_list['SMF123_SERVER_STOKEN'] = """
        SToken of the server (ASS-BSTKN).
        """
        
        
        self.SMF123_SERVER_CONFIG_DIR = ''
        """
        The path to where server.xml for the server is located, this includes the server name.
        """
        self.help_list['SMF123_SERVER_CONFIG_DIR'] = """
        The path to where server.xml for the server is located, this includes the server name.
        """
        
        self.SMF123_SERVER_VERSION = ''
        """
        Version of the server <v.r.m.f>
        """
        self.help_list['SMF123_SERVER_VERSION'] = """
        Version of the server <v.r.m.f>
        """
        
        #### DA QUI IN POI SONO RECORD EFFETTIVAMENTE CHE CONTENGONO I 
        #### DATI DELLE RIGHE VERE E PROPRIE
        
        
        self.SMF123S2_REQ_DATA_VERSION = 1
        """
        Version of request data record. Set to 1.
        """
        self.help_list['SMF123S2_REQ_DATA_VERSION'] = """
        Version of request data record. Set to 1.
        """
        
        
        self.SMF123S2_REQ_APP_TYPE = ''
        """
        Request application type:

        - 1 = CICS®
        - 2 = IMS
        - 3 = ZOS
        """
        self.help_list['SMF123S2_REQ_APP_TYPE'] = """
        Request application type:

        - 1 = CICS®
        - 2 = IMS
        - 3 = ZOS
        """
        
        
        self.SMF123S2_HTTP_RESP_CODE = ''
        """
        HTTP response code returned from the API endpoint.
        """
        self.help_list['SMF123S2_HTTP_RESP_CODE'] = """
        HTTP response code returned from the API endpoint.
        """
        
        
        self.SMF123S2_REQ_STATUS_CODE = ''
        """
        HTTP status code returned to the z/OS application.
        """
        self.help_list['SMF123S2_REQ_STATUS_CODE'] = """
        HTTP status code returned to the z/OS application.
        """
        
        
        self.SMF123S2_RESP_FLAGS = ''
        """
        Response flags.
        """
        self.help_list['SMF123S2_RESP_FLAGS'] = """
        Response flags.
        """
        
        
        self.SMF123S2_REQ_RETRIED = ''
        """
        Set if the request to the API endpoint was retried after a 401 authentication
         failure.
        """
        self.help_list['SMF123S2_REQ_RETRIED'] = """
        Set if the request to the API endpoint was retried after a 401 authentication
         failure.
        """
                
        
        self.SMF123S2_REQ_PAYLOAD_LEN = 0
        """
        Length of the request payload sent to the API endpoint, in bytes.
        """
        self.help_list['SMF123S2_REQ_PAYLOAD_LEN'] = """
        Length of the request payload sent to the API endpoint, in bytes.
        """
        
        
        self.SMF123S2_RESP_PAYLOAD_LEN = 0
        """
        Length of the response payload received from the API endpoint, in bytes.
        """
        self.help_list['SMF123S2_RESP_PAYLOAD_LEN'] = """
        Length of the response payload received from the API endpoint, in bytes.
        """
        
        
        self.SMF123S2_USER_NAME = ''
        """
        The value is one of the following:
        
        - The authenticated username.
        - From V3.0.58.0, when apiRequesterEarlyFailure="true" is configured:
            - For a request that fails basic authentication with the z/OS Connect 
              server, with a 401 response code due to invalid credentials, the 
              username from the credentials in the Authorization header.
            - The unauthenticated username.
        """
        self.help_list['SMF123S2_USER_NAME'] = """
        The value is one of the following:
        
        - The authenticated username.
        - From V3.0.58.0, when apiRequesterEarlyFailure="true" is configured:
            - For a request that fails basic authentication with the z/OS Connect 
              server, with a 401 response code due to invalid credentials, the 
              username from the credentials in the Authorization header.
            - The unauthenticated username.
        """
        
                
        self.SMF123S2_USER_NAME_MAPPED = ''
        """
        If a distributed ID was sent on the request and is mapped to a SAF username, 
        then this value is the authenticated SAF username. Otherwise, this value is blank.
        """
        self.help_list['SMF123S2_USER_NAME_MAPPED'] = """
        If a distributed ID was sent on the request and is mapped to a SAF username, 
        then this value is the authenticated SAF username. Otherwise, this value is blank.
        """
        
        
        self.SMF123S2_USER_NAME_ASSERTED = ''
        """
        z/OS application asserted user ID.
        """
        self.help_list['SMF123S2_USER_NAME_ASSERTED'] = """
        z/OS application asserted user ID.
        """
        
        
        self.SMF123S2_API_REQ_NAME = ''
        """
        API requester name.
        """
        self.help_list['SMF123S2_API_REQ_NAME'] = """
        API requester name.
        """
        
        
        self.SMF123S2_API_REQ_VERSION = ''
        """
        API requester version.
        """
        self.help_list['SMF123S2_API_REQ_VERSION'] = """
        API requester version.
        """
        
        
        self.SMF123S2_ENDPOINT_REFERENCE = ''
        """
        Reference to the element in server.xml that identifies the connection to the API endpoint.
        """
        self.help_list['SMF123S2_ENDPOINT_REFERENCE'] = """
        Reference to the element in server.xml that identifies the connection to the API endpoint.
        """
        
        
        self.SMF123S2_ENDPOINT_HOST = ''
        """
        The value of the host property of the API endpoint.
        """
        self.help_list['SMF123S2_ENDPOINT_HOST'] = """
        The value of the host property of the API endpoint.
        """
        
        
        self.SMF123S2_ENDPOINT_PORT = ''
        """
        The value of the port property of the API endpoint.
        """
        self.help_list['SMF123S2_ENDPOINT_PORT'] = """
        The value of the port property of the API endpoint.
        """
        
        
        self.SMF123S2_ENDPOINT_FULL_PATH = ''
        """
        The full path invoked on the API endpoint.
        """
        self.help_list['SMF123S2_ENDPOINT_FULL_PATH'] = """
        The full path invoked on the API endpoint.
        """
        
        
        self.SMF123S2_ENDPOINT_METHOD = ''
        """
        The HTTP method used for the API endpoint request, GET/POST/PUT/DELETE/OPTIONS.
        """
        self.help_list['SMF123S2_ENDPOINT_METHOD'] = """
        The HTTP method used for the API endpoint request, GET/POST/PUT/DELETE/OPTIONS.
        """
        
        
        self.SMF123S2_ENDPOINT_QUERY_STR = ''
        """
        The query string that is passed to the API endpoint.
        """
        self.help_list['SMF123S2_ENDPOINT_QUERY_STR'] = """
        The query string that is passed to the API endpoint.
        """
        
        
        self.SMF123S2_TIME_STUB_SENT = ''
        """
        Time the request left the calling application. (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_STUB_SENT'] = """
        Time the request left the calling application. (zos binary time format)
        """
        
        # self.UTC_CONV_TIME_STUB_SENT = datetime.min
        self.UTC_CONV_TIME_STUB_SENT = ''
        """
        Time the request left the calling application. 
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_STUB_SENT'] = """
        Time the request left the calling application. 
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        
        self.SMF123S2_TIME_ZC_ENTRY = datetime.min
        """
        Time of IBM z/OS Connect Entry. (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_ZC_ENTRY'] = """
        Time of IBM z/OS Connect Entry. (zos binary time format)
        """
        
        # self.UTC_CONV_TIME_ZC_ENTRY = datetime.min
        self.UTC_CONV_TIME_ZC_ENTRY = ''
        """
        Time of IBM z/OS Connect Entry.  
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_ZC_ENTRY'] = """
        Time of IBM z/OS Connect Entry.  
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        self.ELAPSED_ZC_ENTRY_TO_STUB = Decimal(0)
        """
        Campo Calcolato: Differenza UTC_CONV_TIME_ZC_ENTRY - UTC_CONV_TIME_STUB_SENT:
        Tempo totale trascorso dall'avvio dello stub per Zconnect e la ricezione 
        da parte di zconnect della richiesta (secondi).
        Estrazione del tempo trascorso tra l'avvio dello stub e la ricezione
        della richiesta su zConnect.
        """
        self.help_list['ELAPSED_ZC_ENTRY_TO_STUB'] = """
        Campo Calcolato: Differenza UTC_CONV_TIME_ZC_ENTRY - UTC_CONV_TIME_STUB_SENT:
        Tempo totale trascorso dall'avvio dello stub per Zconnect e la ricezione 
        da parte di zconnect della richiesta (secondi).
        Estrazione del tempo trascorso tra l'avvio dello stub e la ricezione
        della richiesta su zConnect.
        """
        
        self.SMF123S2_TIME_ZC_EXIT = datetime.min
        """
        Time of IBM z/OS Connect Exit. (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_ZC_EXIT'] = """
        Time of IBM z/OS Connect Exit. (zos binary time format)
        """
        
        self.UTC_CONV_TIME_ZC_EXIT = datetime.min
        """
        Time of IBM z/OS Connect Exit.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_ZC_EXIT'] = """
        Time of IBM z/OS Connect Exit.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        self.ELAPSED_ENDPOINT_SENT_ZC_ENTRY = Decimal(0)
        """
        Estrazione del tempo trascorso tra la ricezione della richiesta su zConnect
        e la chiamata al servizio sull'endpoint. (tempo impiegato da zconnect per spedire
        la chiamata). (UTC_CONV_TIME_ENDPOINT_SENT - UTC_CONV_TIME_ZC_ENTRY)
        """
        self.help_list['ELAPSED_ENDPOINT_SENT_ZC_ENTRY'] = """
        Estrazione del tempo trascorso tra la ricezione della richiesta su zConnect
        e la chiamata al servizio sull'endpoint. (tempo impiegato da zconnect per spedire
        la chiamata). (UTC_CONV_TIME_ENDPOINT_SENT - UTC_CONV_TIME_ZC_ENTRY)
        """

        
        self.ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED = datetime.min
        """
        Estrazione del tempo trascorso tra la ricezione della richiesta su zConnect
        e la chiamata al servizio sull'endpoint. (tempo impiegato da zconnect per spedire
        la chiamata). (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_ENDPOINT_RECEIVED)
        """
        self.help_list['ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED'] = """
        Estrazione del tempo trascorso tra la ricezione della richiesta su zConnect
        e la chiamata al servizio sull'endpoint. (tempo impiegato da zconnect per spedire
        la chiamata). (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_ENDPOINT_RECEIVED)
        """
        
        
        self.ELAPSED_ZC_AND_ENDPOINT = datetime.min
        """
        Estrazione del tempo totale dalla chiamata a zconnect alla restituzione del 
        output al chiamante, incluso il tempo speso dall'endpoint per rispondere.
        (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_ZC_ENTRY)
        """
        self.help_list['ELAPSED_ZC_AND_ENDPOINT'] = """
        Estrazione del tempo totale dalla chiamata a zconnect alla restituzione del 
        output al chiamante, incluso il tempo speso dall'endpoint per rispondere.
        (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_ZC_ENTRY)
        """
        
        
        self.ELAPSED_TOTAL = datetime.min
        """
        Estrazione del tempo totale end to end dalla esecuzione dello
        stub chiamante al ritorno della risposta al chiamante da parte 
        di zconnect, inclusi tutti i tempi di risposta dello stub, di 
        zconnect ed anche dell'endpoint chiamato.
        (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_STUB_SENT)
        """
        self.help_list['ELAPSED_TOTAL'] = """
        Estrazione del tempo totale end to end dalla esecuzione dello
        stub chiamante al ritorno della risposta al chiamante da parte 
        di zconnect, inclusi tutti i tempi di risposta dello stub, di 
        zconnect ed anche dell'endpoint chiamato.
        (UTC_CONV_TIME_ZC_EXIT - UTC_CONV_TIME_STUB_SENT)
        """
        
        
        self.ELAPSED_STUB_AND_ZC = datetime.min
        """
        Differenza tra il tempo totale ed il tempo speso dall'endpoint. Identifica
        il tempo totale speso tra stub e zconnect al netto del tempo impiegato dallo
        endpoint chiamato per restituire i dati.
        (ELAPSED_TOTAL - ELAPSED_ENDPOINT_RECEIVED_ENDPOINT_SENT)
        """
        self.help_list['ELAPSED_STUB_AND_ZC'] = """
        Differenza tra il tempo totale ed il tempo speso dall'endpoint. Identifica
        il tempo totale speso tra stub e zconnect al netto del tempo impiegato dallo
        endpoint chiamato per restituire i dati.
        (ELAPSED_TOTAL - ELAPSED_ENDPOINT_RECEIVED_ENDPOINT_SENT)
        """
        
        self.SMF123S2_TIME_TOKEN_GET_START = datetime.min
        """
        Time IBM z/OS Connect started to obtain one or more access tokens.
        (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_TOKEN_GET_START'] = """
        Time IBM z/OS Connect started to obtain one or more access tokens.
        (zos binary time format)
        """
        
        self.UTC_CONV_TIME_TOKEN_GET_START = datetime.min
        """
        Time IBM z/OS Connect started to obtain one or more access tokens.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_TOKEN_GET_START'] = """
        Time IBM z/OS Connect started to obtain one or more access tokens.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        
        self.SMF123S2_TIME_TOKEN_GET_FINISH = datetime.min
        """
        Time IBM z/OS Connect completed obtaining the access token(s).
        (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_TOKEN_GET_FINISH'] = """
        Time IBM z/OS Connect completed obtaining the access token(s).
        (zos binary time format)
        """
        
        self.UTC_CONV_TIME_TOKEN_GET_FINISH = datetime.min
        """
        Time IBM z/OS Connect completed obtaining the access token(s).
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_TOKEN_GET_FINISH'] = """
        Time IBM z/OS Connect completed obtaining the access token(s).
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        
        self.SMF123S2_TIME_ENDPOINT_SENT = datetime.min
        """
        Time IBM z/OS Connect sent the request to the endpoint.
        (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_ENDPOINT_SENT'] = """
        Time IBM z/OS Connect sent the request to the endpoint.
        (zos binary time format)
        """
        
        self.UTC_CONV_TIME_ENDPOINT_SENT = datetime.min
        """
        Time IBM z/OS Connect sent the request to the endpoint.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_ENDPOINT_SENT'] = """
        Time IBM z/OS Connect sent the request to the endpoint.
        (converted to UTC format time: e.g: 2023/06/28 09:25:34.844246 UTC)
        """
        
        self.ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT = Decimal(0)
        """
        Estrazione della differenza tra il tempo di spedizione all'endpoint
        ed il tempo di ricezione dall'endpoint. Tempo totale speso dall'endpoint
        in secondi (UTC_CONV_TIME_ENDPOINT_RECEIVED - UTC_CONV_TIME_ENDPOINT_SENT)
        """
        self.help_list['ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT'] = """
        Estrazione della differenza tra il tempo di spedizione all'endpoint
        ed il tempo di ricezione dall'endpoint. Tempo totale speso dall'endpoint
        in secondi (UTC_CONV_TIME_ENDPOINT_RECEIVED - UTC_CONV_TIME_ENDPOINT_SENT)
        """
        
        self.SMF123S2_TIME_ENDPOINT_RECEIVED = datetime.min
        """
        Time IBM z/OS Connect received a response from the endpoint.
        (zos binary time format)
        """
        self.help_list['SMF123S2_TIME_ENDPOINT_RECEIVED'] = """
        Time IBM z/OS Connect received a response from the endpoint.
        (zos binary time format)
        """
        
        self.UTC_CONV_TIME_ENDPOINT_RECEIVED = datetime.min
        """
        Time IBM z/OS Connect received a response from the endpoint.
        (converted to UTC format time: e.g.: 2023/06/28 09:25:34.844246 UTC)
        """
        self.help_list['UTC_CONV_TIME_ENDPOINT_RECEIVED'] = """
        Time IBM z/OS Connect received a response from the endpoint.
        (converted to UTC format time: e.g.: 2023/06/28 09:25:34.844246 UTC)
        """
        
        self.SMF123S2_MVS_JOBNAME = ''
        """
        MVS Job Name of the calling application (JSAB -> JSABJBNM).
        """
        self.help_list['SMF123S2_MVS_JOBNAME'] = """
        MVS Job Name of the calling application (JSAB -> JSABJBNM).
        """
        
        
        self.SMF123S2_MVS_JOBID = ''
        """
        MVS Job ID of the calling application (JSAB -> JSABJBID).
        """
        self.help_list['SMF123S2_MVS_JOBID'] = """
        MVS Job ID of the calling application (JSAB -> JSABJBID).
        """
        
        
        self.SMF123S2_MVS_SYSNAME = ''
        """
        MVS System Name of the calling application (CVT -> CVTSNAME).
        """
        self.help_list['SMF123S2_MVS_SYSNAME'] = """
        MVS System Name of the calling application (CVT -> CVTSNAME).
        """
        
        
        self.SMF123S2_MVS_ASID = ''
        """
        MVS ASID of the calling application (ASCB -> ASCBASID).
        """
        self.help_list['SMF123S2_MVS_ASID'] = """
        MVS ASID of the calling application (ASCB -> ASCBASID).
        """
        
        
        self.SMF123S2_MVS_SID = ''
        """
        MVS SID of the calling application (SMCA -> SMCASID).
        """
        self.help_list['SMF123S2_MVS_SID'] = """
        MVS SID of the calling application (SMCA -> SMCASID).
        """
        
        
        self.SMF123S2_CICS_APPLID = ''
        """
        The APPLID of the CICS region.
        """
        self.help_list['SMF123S2_CICS_APPLID'] = """
        The APPLID of the CICS region.
        """
        
        
        self.SMF123S2_CICS_TASK_NUMBER = ''
        """
        The CICS task number of the calling application.
        """
        self.help_list['SMF123S2_CICS_TASK_NUMBER'] = """
        The CICS task number of the calling application.
        """
        
        
        self.SMF123S2_CICS_TRANSID = ''
        """
        The CICS transaction ID of the calling application.
        """
        self.help_list['SMF123S2_CICS_TRANSID'] = """
        The CICS transaction ID of the calling application.
        """
        
        
        self.SMF123S2_CICS_RMUOWID = ''
        """
        The CICS Recovery Manager UOW ID of the calling application. For correlation with CICS.
        It is possible to correlate the SMF 123 subtype 2 record with data from CICS and IMS systems.
        - For CICS, the data run time that is required for correlation can be obtained by using the 
          CEMT INQUIRE TASK system command. CICS also records this information in the RMUOWID, NETUOWPX, 
          and NETUOWSX fields of the DFHTASK group in the PERFORMANCE class of SMF 110 SubType 1 records.
        - For IMS, the recovery token represents the work performed within a commit interval and is 
          available in the IMS log records written to the IMS log.
        """
        self.help_list['SMF123S2_CICS_RMUOWID'] = """
        The CICS Recovery Manager UOW ID of the calling application. For correlation with CICS.
        It is possible to correlate the SMF 123 subtype 2 record with data from CICS and IMS systems.
        - For CICS, the data run time that is required for correlation can be obtained by using the 
          CEMT INQUIRE TASK system command. CICS also records this information in the RMUOWID, NETUOWPX, 
          and NETUOWSX fields of the DFHTASK group in the PERFORMANCE class of SMF 110 SubType 1 records.
        - For IMS, the recovery token represents the work performed within a commit interval and is 
          available in the IMS log records written to the IMS log.
        """
        
        
        self.SMF123S2_CICS_NETUOW_PX = ''
        """
        CICS Network UOW Prefix of the calling application. For correlation with CICS.
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.  
        """
        self.help_list['SMF123S2_CICS_NETUOW_PX'] = """
        CICS Network UOW Prefix of the calling application. For correlation with CICS.
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.  
        """
        
        
        self.SMF123S2_CICS_NETUOW_SX = ''
        """
        CICS Network UOW Suffix of the calling application. For correlation with CICS
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.        
        """
        self.help_list['SMF123S2_CICS_NETUOW_SX'] = """
        CICS Network UOW Suffix of the calling application. For correlation with CICS
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.        
        """
                     
        
        self.SMF123S2_IMS_IDENTIFIER = ''
        """
        The identifier from the execution parameters of the calling application.
        """
        self.help_list['SMF123S2_IMS_IDENTIFIER'] = """
        The identifier from the execution parameters of the calling application.
        """
        
        
        self.SMF123S2_IMS_REGION_ID = 0
        """
        The region identifier of the calling application.
        """
        self.help_list['SMF123S2_IMS_REGION_ID'] = """
        The region identifier of the calling application.
        """
        
        
        self.SMF123S2_IMS_TRANSNAME = 0
        """
        The transaction name of the calling application.
        """
        self.help_list['SMF123S2_IMS_TRANSNAME'] = """
        The transaction name of the calling application.
        """
        
        
        self.SMF123S2_IMS_APPNAME = ''
        """
        The name of the application.
        """
        self.help_list['SMF123S2_IMS_APPNAME'] = """
        The name of the application.
        """
        
        
        self.SMF123S2_IMS_PSBNAME = ''
        """
        The name of the PSB (Program Specification Block). 
        """
        self.help_list['SMF123S2_IMS_PSBNAME'] = """
        The name of the PSB (Program Specification Block). 
        """
        
        
        self.SMF123S2_IMS_RECOVERY_TOKEN = ''
        """
        The recovery token for the UOW of the calling application.
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.  
        """
        self.help_list['SMF123S2_IMS_RECOVERY_TOKEN'] = """
        The recovery token for the UOW of the calling application.
        - It is possible to correlate the SMF 123 subtype 2 record with data from CICS and 
        IMS systems.
          - For CICS, the data run time that is required for correlation can be obtained by 
          using the CEMT INQUIRE TASK system command. CICS also records this information in 
          the RMUOWID, NETUOWPX, and NETUOWSX fields of the DFHTASK group in the PERFORMANCE 
          class of SMF 110 SubType 1 records.
          - For IMS, the recovery token represents the work performed within a commit interval 
          and is available in the IMS log records written to the IMS log.  
        """
        
        
        self.SMF123S2_REQ_ID = ''
        """
        Request identifier that is unique within a IBM z/OS Connect server instance.
        """
        self.help_list['SMF123S2_REQ_ID'] = """
        Request identifier that is unique within a IBM z/OS Connect server instance.
        """
        
        
        self.SMF123S2_TRACKING_TOKEN = ''
        """
        Tracking token.
        """
        self.help_list['SMF123S2_TRACKING_TOKEN'] = """
        Tracking token.
        """
        
        
        self.SMF123S2_REQ_HDR1 = ''
        """
        Request header. <header1name>:<header1value>
        """
        self.help_list['SMF123S2_REQ_HDR1'] = """
        Request header. <header1name>:<header1value>
        """

        
        self.SMF123S2_REQ_HDR2 = ''
        """
        Request header. <header2name>:<header2value>
        """
        self.help_list['SMF123S2_REQ_HDR2'] = """
        Request header. <header2name>:<header2value>
        """

        
        self.SMF123S2_REQ_HDR3 = ''
        """
        Request header. <header3name>:<header3value>
        """
        self.help_list['SMF123S2_REQ_HDR3'] = """
        Request header. <header3name>:<header3value>
        """

        
        self.SMF123S2_REQ_HDR4 = ''
        """
        Request header. <header4name>:<header4value>
        """
        self.help_list['SMF123S2_REQ_HDR4'] = """
        Request header. <header4name>:<header4value>
        """  
        
        
        self.SMF123S2_RESP_HDR1 = ''
        """
        Response header. <header1name>:<header1value>
        """
        self.help_list['SMF123S2_RESP_HDR1'] = """
        Response header. <header1name>:<header1value>
        """
        
        
        self.SMF123S2_RESP_HDR2 = ''
        """
        Response header. <header2name>:<header2value>
        """
        self.help_list['SMF123S2_RESP_HDR2'] = """
        Response header. <header2name>:<header2value>
        """
        
        
        self.SMF123S2_RESP_HDR3 = ''
        """
        Response header. <header2name>:<header2value>
        """
        self.help_list['SMF123S2_RESP_HDR3'] = """
        Response header. <header3name>:<header3value>
        """
        
        
        self.SMF123S2_RESP_HDR4 = ''
        """
        Response header. <header4name>:<header4value>
        """
        self.help_list['SMF123S2_RESP_HDR4'] = """
        Response header. <header4name>:<header4value>
        """
        
        self.CLONE = ''
        """
        Clone ISP da cui la chiamata è stata inoltrata.
        """
        self.help_list['CLONE'] = """
        Clone ISP da cui la chiamata è stata inoltrata.
        """
        
    def carica_parte_fissa(self,
      p_SMF123_SID: str,
      p_SMF123_SERVER_SYSTEM: str,
      p_SMF123_SERVER_SYSPLEX: str,
      p_SMF123_SERVER_JOBID: str,
      p_SMF123_SERVER_JOBNAME: str,
      p_SMF123_SERVER_STOKEN: str,
      p_SMF123_SERVER_CONFIG_DIR: str,
      p_SMF123_SERVER_VERSION: str,
    ):
      self.SMF123_SID = p_SMF123_SID
      self.SMF123_SERVER_SYSTEM = p_SMF123_SERVER_SYSTEM
      self.SMF123_SERVER_SYSPLEX = p_SMF123_SERVER_SYSPLEX
      self.SMF123_SERVER_JOBID = p_SMF123_SERVER_JOBID
      self.SMF123_SERVER_JOBNAME = p_SMF123_SERVER_JOBNAME
      self.SMF123_SERVER_STOKEN = p_SMF123_SERVER_STOKEN
      self.SMF123_SERVER_CONFIG_DIR = p_SMF123_SERVER_CONFIG_DIR
      self.SMF123_SERVER_VERSION = p_SMF123_SERVER_VERSION
    
if __name__ == '__main__':  
    print('STARTING TEST')
    _rec = Record_smf()
    print(f'SMF123_SERVER_CONFIG_DIR.__doc__: {_rec.SMF123_SERVER_CONFIG_DIR.__doc__}')
    print(f'help_list["SMF123_SERVER_CONFIG_DIR"]: {_rec.help_list["SMF123_SERVER_CONFIG_DIR"]}')
    # print(_rec.__class__)
    # print(_rec.__dict__)
    # print(_rec.__class__.__dict__['RMITOTAL'].__doc__)
    print('ENDING TEST')
    