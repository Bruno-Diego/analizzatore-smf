# PROGRAMMA ANALIZZATORE_SMF_123_2

## DESCRIZIONE DEL PROGRAMMA

Il programma effettua la analisi dei files SMF 123.2 e li trasforma in file di excel

## SINTASSI

Il programma viene richiamato come : 

```cmd
analizzatore_smf_123_2.py -f <input_file> -e <excelfile.xlsx>
```

Quando viene eseguito in questa modalità, il programma esegue le seguenti azioni:

1. Apre il file di input (in formato salvataggio SMF dal mainframe)
2. Estrae i record SMF
3. Trasforma i campi SMF in colonne di una base dati
4. Filtra ed estrae solamente i campi (di default) : SMF123_SERVER_JOBID, SMF123S2_API_REQ_NAME, SMF123S2_HTTP_RESP_CODE, SMF123S2_REQ_STATUS_CODE, SMF123S2_ENDPOINT_REFERENCE, SMF123S2_ENDPOINT_HOST, SMF123S2_ENDPOINT_METHOD, UTC_CONV_TIME_STUB_SENT, UTC_CONV_TIME_ZC_ENTRY, ELAPSED_STUB_TO_ZC_ENTRY, UTC_CONV_TIME_ENDPOINT_SENT, ELAPSED_ENDPOINT_SENT_ZC_ENTRY, UTC_CONV_TIME_ENDPOINT_RECEIVED, ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT, UTC_CONV_TIME_ZC_EXIT, ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED, ELAPSED_ZC_AND_ENDPOINT, ELAPSED_TOTAL, CLONE, SMF123S2_MVS_JOBNAME, SMF123S2_MVS_JOBID, SMF123S2_CICS_APPLID, SMF123S2_CICS_TASK_NUMBER, SMF123S2_CICS_TRANSID
5. Salva il contenuto in un file di excel.

Il programma ha alcuni parametri opzionali che possono essere specificati per eseguire le seguenti funzioni: 

- `-c, --changelog` : Visualizza il log delle modifiche del programma ed esce senza
  eseguire alcuna altra operazione.
- `-f, --smf-file TEXT` : Specifica File di ingresso con estrazione SMF. Obbligatoria, deve
  sempre essere specificato o il programma dichiara un errore.
- `-e, --excel-file TEXT` : Specifica il file di uscita excel. E' sempre necessario aggiungere 
l'estensione .xlsx.
- `-l, --field-list TEXT` : Specifica l'elenco di nomi di campi SMF, separati da |. Questa 
è un parametro opzionale, se non viene specificato nulla, è equivalente a dare il comando:
  `--field-list "SMF123_SERVER_JOBID|SMF123S2_API_REQ_NAME|SMF123S2_HTTP_RESP_CODE|SMF123S2_REQ_STATUS_CODE|SMF123S2_ENDPOINT_REFERENCE|SMF123S2_ENDPOINT_HOST|SMF123S2_ENDPOINT_METHOD|UTC_CONV_TIME_STUB_SENT|UTC_CONV_TIME_ZC_ENTRY|ELAPSED_STUB_TO_ZC_ENTRY|UTC_CONV_TIME_ENDPOINT_SENT|ELAPSED_ENDPOINT_SENT_ZC_ENTRY|UTC_CONV_TIME_ENDPOINT_RECEIVED|ELAPSED_ENDPOINT_RECEIVED_ENPOINT_SENT|UTC_CONV_TIME_ZC_EXIT|ELAPSED_ZC_EXIT_ENDPOINT_RECEIVED|ELAPSED_ZC_AND_ENDPOINT|ELAPSED_TOTAL|CLONE|SMF123S2_MVS_JOBNAME|SMF123S2_MVS_JOBID|SMF123S2_CICS_APPLID|SMF123S2_CICS_TASK_NUMBER|SMF123S2_CICS_TRANSID"`:
  - La lista dei campi deve essere fra virgolette doppie: p.es:
  `--field-list "SMF123_SERVER_JOBID|SMF123S2_API_REQ_NAME|SMF123S2_HTTP_RESP_CODE..."` ovvero `-f "SMF123_SERVER_JOBID|SMF123S2_API_REQ_NAME|SMF123S2_HTTP_RESP_CODE..."`
- `-a, --field-names` : Visualizza la lista dei nomi dei campi SMF (e dei campi calcolati) con 
  una minima porzione dell'help del relativo campo.
- `-d, --help-field TEXT` : Per il nome di campo specificato, visualizza la descrizione contenuta 
  nel manuale dell'IBM CICS per il relativo campo SMF 110.1, se questa è presente.
- `--version` : Visualizza la versione del programma ed esce senza eseguire alcuna altra operazione.
- `--help` : Visualizza un messaggio di help ed esce senza eseguire alcuna altra operazione.
