from os import system
from pathlib import Path
import sys
from time import sleep
import click
import click_spinner
import pandas as pd

from colorama import just_fix_windows_console
from utils.export_excel import Export_excel

from utils.messages import Messages
from utils.help_print import Help_print
just_fix_windows_console()
from colorama import Fore, Back, Style
from data_layer.record_smf import Record_smf


from estrattore import Estrattore

MARTICCHIO=False
VERSION='1.3.3'
LICENSE='BSD'
CREDITS='Author: M. Viarizzo'
PROGNAME=sys.argv[0]
CHANGELOG = f'''
                          {PROGNAME} VERSIONE {VERSION}
                                CHANGELOG
- v. 1.3.3 @ 2024-05-21   : Modificato gestione SMF 123 Type 1: adesso i record type 1 
                            (e anche altri subtype) vengono ignorati e vengono letti 
                            solo i type 2
- v. 1.3.2 @ 2023-10-17   : Completato con le caratteristiche complete.
- v. 1.3.1 @ 2023-10-17   : Campi tempistiche espongono microsecondi. Cics task number 
                            come numero per ordinare. Blocco pima riga e prima colonna
                            Prima riga autofilter e dimensioni colonne automatiche
- v. 1.2.4 @ 2023-10-11   : Modificato per rilevare gli errori nell'analisi del file.
                            Ci sono alcuni file che hanno come prima intestazione l'header
                            SUBTYPE=1. Basta modificare e dare 2. Al massimo se è errato,
                            allora arriva in fondo e dice che non ce ne sono.
- v. 1.2.3 @ 2023-10-10   : Stampa riga di errore e continua analisi se errore durante 
                            analisi della riga
- v. 1.2.2 @ 2023-10-06   : AGgiunto stampa riga di errore durante l'analisi
- v. 1.2.1 @ 2023-07-17   : Modificato script di build dei sorgenti per includere
                            readme e powershell per misurare le tempistiche.
- v. 1.2.0 @ 2023-07-11   : Aggiunto medie esecuzioni su Foglio raggruppamento.
- v. 1.1.0 @ 2023-07-11   : Aggiunto foglio con raggruppamento per API_REQ_NAME e 
                            totali esecuzione. Aggiunti campi response e campo calcolato
                            CLONE all'excel e aggregato per API_REQ_NAME e CLONE
- v. 1.0.0 @ 2023-07-10   : Versione completa, con standard minimo campi definito
- v. 0.0.3 @ 2023-07-05   : Completato estrattore e aggiunti record calcolati tempistiche
- v. 0.0.2 @ 2023-07-04   : Completato inserimento campi record SMF 123.2
- v. 0.0.1 @ 2023-06-29   : Versione iniziale: Inserimento Campi record SMF 123.2

'''
DATE='2023-10-17'

# @click.command()
# @click.option('-c', '--changelog', 
#               help=f"Visualizza il log delle modifiche del programma.", 
#               is_flag=True, 
#               show_default=True, 
#               default=False,
# )
# @click.option('-n', '--noma', 
#               is_flag=True, 
#               default=False, 
#               hidden=True,
# )
# @click.option('-f', '--smf-file', 
#               nargs=1, 
#               help=f"File di ingresso con estrazione SMF",
# )
# @click.option('-e', '--excel-file', 
#               nargs=1, 
#               help=f"File di uscita excel (aggiungere estensione .xlsx)"
# )
# @click.option('-l', '--field-list', 
#               nargs=1, 
#               help=f"""Elenco di nomi di campi SMF, separati da |. 
# Parametro opzionale, se non specificato è equivalente a specificare: 
    
# --field-list "SMF123_SERVER_JOBID|SMF123S2_API_REQ_NAME|SMF123S2_HTTP_RESP_CODE
# |SMF123S2_REQ_STATUS_CODE|SMF123S2_ENDPOINT_REFERENCE
# |SMF123S2_ENDPOINT_HOST|SMF123S2_ENDPOINT_METHOD|UTC_CONV_TIME_STUB_SENT
# |UTC_CONV_TIME_ZC_ENTRY|ELAPSED_STUB_TO_ZC_ENTRY|UTC_CONV_TIME_ENDPOINT_SENT
# |ELAPSED_ENDPOINT_SENT_ZC_ENTRY|UTC_CONV_TIME_ENDPOINT_RECEIVED
# |ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT|UTC_CONV_TIME_ZC_EXIT
# |ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED|ELAPSED_ZC_AND_ENDPOINT|ELAPSED_TOTAL
# |CLONE|SMF123S2_MVS_JOBNAME|SMF123S2_MVS_JOBID|SMF123S2_CICS_APPLID
# |SMF123S2_CICS_TASK_NUMBER|SMF123S2_CICS_TRANSID|"

# Nota: i nomi dei campi corrispondono a quelli del record SMF 123 type 2, con l'aggiunta di :
# ELAPSED_STUB_TO_ZC_ENTRY, ELAPSED_ENDPOINT_SENT_ZC_ENTRY, ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED,
# ELAPSED_ZC_AND_ENDPOINT, ELAPSED_TOTAL, ELAPSED_STUB_AND_ZC che sono campi calcolati.
# Eseguire il comando {PROGNAME} -d <nome_campo> per ulteriori dettagli su questi campi.
        
# Nota: La lista dei campi deve essere fra virgolette doppie: 
# --field-list "SMF123S2_ENDPOINT_HOST|SMF123S2_API_REQ_NAME|SMF123S2_ENDPOINT_REFERENCE|
# SMF123S2_ENDPOINT_HOST..."               
#               """,
# )
# @click.option('-a', '--field-names',
#               is_flag=True,
#               help=f"""Visualizza la lista dei nomi dei campi SMF (e dei campi calcolati)
#               con una minima porzione dell'help del relativo campo.
#               """
# )
# @click.option('-d', '--help-field',
#               nargs=1, 
#               help=f"""Per il nome di campo specificato, visualizza la descrizione
#               contenuta nel manuale dell'IBM CICS per il relativo campo SMF 110.1,
#               se questa è presente
#               """
# )
# @click.version_option('-V', '--version', 
#                       help=f"Visualizza la versione del programma", 
#                       message=f"\n{PROGNAME}, versione {VERSION} - {DATE}\n{CREDITS}\nLicenza: {LICENSE}\n"
# )
async def analizzatore_smf_123_2(
    input,
    # changelog,
    # smf_file,
    # excel_file,
    # noma,
    # field_list,
    # field_names,
    # help_field,
) : 
    
    _g_HELP_PRINT = Help_print()
    
    # if changelog:
    #     _g_HELP_PRINT.show_changelog()
    #     sys.exit(0)

    # if field_names:
    #     _rec = Record_smf()
    #     _MAX_HELP_LEN = 60
        
    #     print()
    #     print('===============================')
    #     print('LISTA DEI CAMPI SMF 123 GESTITI')
    #     print('===============================')
    #     print()
    #     for _field in _rec.help_list.keys():
    #         _stripped = f'{_field.ljust(10)} : ' + _rec.help_list[_field].strip().replace("\n", " ") 
    #         _help_str = _stripped if len(_stripped) < _MAX_HELP_LEN  else f'{_stripped[0:_MAX_HELP_LEN]}...'
    #         print(_help_str)
        
    #     print("""
    #     Il comando analizzatore_smf_123_2 -d <nome_campo> produce l'help esteso
    #     completo relativo al campo specificato come da descrizione contenuta nei manuali IBM.
    #     (versione 2023-06-30)
    #     """)
        
    #     sys.exit(0)
               
    # if help_field:
    #     _rec = Record_smf()
    #     if help_field not in _rec.help_list.keys():
    #         _g_HELP_PRINT.print_error(f"""il Valore del campo passato: {help_field} non è presente nella lista dei campi gestiti da questa applicazione.""")
    #         sys.exit(-1)

    #     print()
    #     title_str = f'     {help_field}     '
    #     print("=" * len(title_str))
    #     print(title_str)
    #     print("=" * len(title_str))
    #     print(_rec.help_list[help_field].strip())
    #     sys.exit(0)
    
    if input:
        smf_file = input
        # print(smf_file)
        
    if smf_file is None:
        print("\n")
        _g_HELP_PRINT.print_error('Il file di estrazione SMF di input deve essere specificato. ')
        # print(Fore.GREEN + Back.BLACK)
        print("\n")
        _g_HELP_PRINT.show_help()
        sys.exit(-1)
    _g_FILE_SMF = smf_file
    
    # if excel_file is None: 
    #     print("\n")
    #     _g_HELP_PRINT.print_error('Il file di destinazione Excel di output deve essere specificato')
    #     # print(Fore.GREEN + Back.BLACK)
    #     print("\n")
    #     _g_HELP_PRINT.show_help()
    #     sys.exit(-1)
        
    # if not noma and MARTICCHIO:
    #     print('''
    #           WARNING !! MEMORY BOUNDARY EXCEEDED !!
              
    #           MEMORY DUMP:
              
    #                  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
    #         00000000 4D 5A 90 00 03 00 00 00 04 00 00 FF FF 00 00 00
    #         00000010 B8 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00
    #         00000020 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    #         00000030 00 00 00 00 00 00 00 00 00 00 00 08 01 00 00 00
    #         00000040 0E 1F BA 0E 00 B4 09 CD 21 B8 01 4C CD 21 54 68
    #         00000050 69 73 20 70 72 6F 67 72 61 6D 20 63 61 6E 6E 6F
    #         00000060 74 20 62 65 2E 0D 0D 0A 24 00 00 00 00 00 00 00
    #         00000070 6D 6F 64 65 2E 0D 0A 24 00 00 00 00 00 00 00 00
    #         00000080 CB A9 BE 84 8F C8 D0 D7 C4 B0 D5 D6 31 C8 D0 D7
    #         --------
    #         Dump Error !!!!
    #     ''')
        
    #     sleep(1)
        
    #     print('''
    #           DUMP ERROR !!!
              
    #           YOUR SYSTEM IS AT RISK OF CORRUPTION !!!!
              
    #           FOR SYSTEM SAFETY YOUR SYSTEM WILL BE STOPPED IMMEDIATELY.
    #     ''')
    #     sleep(0.5)
    #     # print('shutdown /P')
    #     system('shutdown /P')
    #     sys.exit(-1)
        

    
    # if field_list is not None:
    #     __list_of_fields = field_list.split('|')
        
    __list_of_fields = [
        'SMF123_SERVER_JOBID', 
        'SMF123S2_API_REQ_NAME', 
        'SMF123S2_HTTP_RESP_CODE',
        'SMF123S2_REQ_STATUS_CODE',
        'SMF123S2_ENDPOINT_REFERENCE', 
        'SMF123S2_ENDPOINT_HOST', 
        'SMF123S2_ENDPOINT_METHOD', 
        'UTC_CONV_TIME_STUB_SENT', 
        'UTC_CONV_TIME_ZC_ENTRY', 
        'ELAPSED_ZC_ENTRY_TO_STUB',
        'UTC_CONV_TIME_ENDPOINT_SENT',
        'ELAPSED_ENDPOINT_SENT_ZC_ENTRY',
        'UTC_CONV_TIME_ENDPOINT_RECEIVED',
        'ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT',
        'UTC_CONV_TIME_ZC_EXIT',
        'ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED',
        'ELAPSED_ZC_AND_ENDPOINT',
        'ELAPSED_TOTAL',
        'CLONE',
        'SMF123S2_MVS_JOBNAME',
        'SMF123S2_MVS_JOBID',
        'SMF123S2_CICS_APPLID',
        'SMF123S2_CICS_TASK_NUMBER',
        'SMF123S2_CICS_TRANSID',
    ]
        
    _list_of_fields = []
        
    _rec = Record_smf()
    for _field in __list_of_fields:
        if _field not in _rec.__dict__.keys():
            _g_HELP_PRINT.print_warn(f'Il campo {_field} non è presente tra i record SMF trattati')
        else:
            _list_of_fields.append(_field)

        
    _g_FILE_EXCEL = input #excel_file
    
    # Verifica errori files
    
    # _path_file_smf= Path(_g_FILE_SMF)
    # if not _path_file_smf.exists():
    #     _g_HELP_PRINT.print_error(f'IL FILE SMF {_g_FILE_SMF} NON ESISTE') 
    #     sys.exit(-2)
    
    try:
        _g_msg = Messages()
        _estrattore = Estrattore(_g_FILE_SMF, _g_msg)
        
        # print(Fore.GREEN + Back.BLACK)
        _g_HELP_PRINT.print_info('Inizio Caricamento File..')
        with click_spinner.spinner():
            _estrattore.load_testo()
    except Exception as e:
        _g_HELP_PRINT.print_error(f'Impossibile caricare il file SMF {_g_FILE_SMF}: {str(e)}')
        sys.exit(-3)
        
    _g_HELP_PRINT.print_info('Interpretazione righe')
    with click_spinner.spinner():
        if (_retval := _estrattore.interpreta_righe()) != 'OK':
            _g_HELP_PRINT.print_error(f'Errore Interpretazione righe: {_retval}')
    
    _g_HELP_PRINT.print_info('Conversione ed estrazione colonne')
    if len(_estrattore.lista_records) == 0:
        _g_HELP_PRINT.print_error(f'Nessun record estratto per il file SMF {_g_FILE_SMF}')
        sys.exit(-4)
        
    with click_spinner.spinner():
        lista_smf_dict = [x.__dict__ for x in _estrattore.lista_records]
        df = pd.DataFrame.from_dict(lista_smf_dict)
        df = df[_list_of_fields]
        # print(df)
        
        # Conversione campi timedelta in float
        if 'ELAPSED_ZC_ENTRY_TO_STUB' in _list_of_fields: 
            df[['ELAPSED_ZC_ENTRY_TO_STUB']] = df[['ELAPSED_ZC_ENTRY_TO_STUB']].astype('float64')
            
        if 'SMF123S2_TIME_ZC_ENTRY' in _list_of_fields:
            df[['SMF123S2_TIME_ZC_ENTRY']] = df[['SMF123S2_TIME_ZC_ENTRY']].astype('float64')
            
        if 'ELAPSED_ZC_ENTRY_TO_STUB' in _list_of_fields:
            df[['ELAPSED_ZC_ENTRY_TO_STUB']] = df[['ELAPSED_ZC_ENTRY_TO_STUB']].astype('float64')
            
        if 'ELAPSED_ENDPOINT_SENT_ZC_ENTRY' in _list_of_fields:
            df[['ELAPSED_ENDPOINT_SENT_ZC_ENTRY']] = df[['ELAPSED_ENDPOINT_SENT_ZC_ENTRY']].astype('float64')
            
        if 'ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED' in _list_of_fields:
            df[['ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED']] = df[['ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED']].astype('float64')
            
        if 'ELAPSED_ZC_AND_ENDPOINT' in _list_of_fields:
            df[['ELAPSED_ZC_AND_ENDPOINT']] = df[['ELAPSED_ZC_AND_ENDPOINT']].astype('float64')
            
        if 'ELAPSED_TOTAL' in _list_of_fields:
            df[['ELAPSED_TOTAL']] = df[['ELAPSED_TOTAL']].astype('float64')
            
        if 'ELAPSED_STUB_AND_ZC' in _list_of_fields:
            df[['ELAPSED_STUB_AND_ZC']] = df[['ELAPSED_STUB_AND_ZC']].astype('float64')
            
        if 'ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT' in _list_of_fields:
            df[['ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT']] = df[['ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT']].astype('float64')
            
        if 'SMF123S2_CICS_TASK_NUMBER' in _list_of_fields:
            df['SMF123S2_CICS_TASK_NUMBER'] = pd.to_numeric(df['SMF123S2_CICS_TASK_NUMBER'])
            
        if 'SMF123S2_HTTP_RESP_CODE' in _list_of_fields:
            df['SMF123S2_HTTP_RESP_CODE'] = pd.to_numeric(df['SMF123S2_HTTP_RESP_CODE'])
            
        if 'SMF123S2_REQ_STATUS_CODE' in _list_of_fields:
            df['SMF123S2_REQ_STATUS_CODE'] = pd.to_numeric(df['SMF123S2_REQ_STATUS_CODE'])
                    
    _g_HELP_PRINT.print_info('Calcolo Esecuzioni e medie')
    with click_spinner.spinner():
        # Raggruppamenti dei campi
        _df_api_req_name = df.groupby(['SMF123S2_API_REQ_NAME','CLONE'])['SMF123S2_API_REQ_NAME'].count().reset_index(name='Num. Esecuzioni')
        _df_api_mean = df.groupby(['SMF123S2_API_REQ_NAME','CLONE'])['ELAPSED_TOTAL'].mean().reset_index(name='Tempo Medio Esecuzione')
        _df_api_req_name['Tempo Medio Esecuzione'] = _df_api_mean['Tempo Medio Esecuzione']
        _df_api_req_name = _df_api_req_name.sort_values(['Num. Esecuzioni'], ascending=False)
    _g_HELP_PRINT.print_info('Send to template.')
    with click_spinner.spinner():
        # Send to template.
        try:
            # Convert DataFrame to NumPy array
            header_array = df
            array_representation = df.to_numpy()
            medie_header = _df_api_req_name
            medie_df = _df_api_req_name.to_numpy()
            
        except Exception as e:
            _g_HELP_PRINT.print_error(f'Impossibile scrivere il file excel "document.xlsx": {str(e)}')
            sys.exit(-4)  
    _g_HELP_PRINT.print_info('Export su excel')
    with click_spinner.spinner():
        # Export to excel
        try:
            with pd.ExcelWriter(_g_FILE_EXCEL) as xlswriter:
                df.to_excel(xlswriter, sheet_name='Dettaglio Chiamate')
                _df_api_req_name.to_excel(xlswriter, sheet_name='Numeri Richieste API')
            _exceller = Export_excel()
            returned_writer = _exceller.export_excel(
                'document.xlsx', 
                df, 
                'Dettaglio Chiamate',
                'Numeri Richieste API',
                _df_api_req_name
            )

        except Exception as e:
            _g_HELP_PRINT.print_error(f'Impossibile scrivere il file excel "document.xlsx": {str(e)}')
            sys.exit(-4)
    
    _g_HELP_PRINT.print_info(f'Conversione del file {_g_FILE_SMF} => "document.xlsx" completata.')
    return (
                header_array, 
                array_representation, 
                medie_header, 
                medie_df,
                df, 
                'Dettaglio Chiamate',
                'Numeri Richieste API',
                _df_api_req_name,
                returned_writer
            )
    
    
# def show_help():
#     ctx = click.get_current_context()
#     click.echo(ctx.get_help())
#     ctx.exit()
    
# def show_changelog():
#     print(CHANGELOG)
        
# def print_error(p_error: str):
#     print(Fore.RED + f' ERRORE : {p_error}')
#     print(Style.RESET_ALL)
    
# def print_warn(p_warn: str):
#     print(Fore.YELLOW + f' WARNING : {p_warn}')
#     print(Style.RESET_ALL)
    
# def print_info(p_info: str):
#     print(Fore.GREEN + f'INFO : {p_info}')
#     print(Style.RESET_ALL)
    
if __name__ == '__main__':
    analizzatore_smf_123_2()