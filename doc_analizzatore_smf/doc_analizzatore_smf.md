<div class="title">DOCUMENTAZIONE ANALIZZATORE SMF</div>

<div class="author">AUTORE: M. Viarizzo</div>

# 1 - INDICE DEI CONTENUTI

[[TOC]]

# 2 - INTRODUZIONE

Questo documento definisce la programmazione per il programma di analisi per il record smf 123 relativo a zosConnect

# 3 - CAMPI DA GESTIRE

- `TRAN`
- `START`
- `STOP`
- `TRANNUM`
- `PGMNAME`
- `OAPPLID`
- `USRCPUT`

Per renderlo più generico, è necessario ricevere un parametro da linea di comando con il TRANID  (che corrisponde al campo TRAN)

# 4 - DESCRIZIONE DEI CAMPI

Record SMF 123 Type 2 : <https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=usrmr-api-requester-data-from-smf-type-1232-v2-records>

# 5 - NOTA

Nel job di estrazione del record SMF, ricordarsi di aggiungere (2): questo estrae solo il subtype 2, altirmenti va in errore. Per il subtype 1, estrarre aggiungendo (1) e utilizzare l'estrattore per il type 1 altrimenti va in errore.