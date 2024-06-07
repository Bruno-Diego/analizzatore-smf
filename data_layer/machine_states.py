class Machine_states(object):
    """
    # Machine_states
    
    Stati della macchina a stati per la conversione dei record
    SMF 110 Subtype 1
    """
    def __init__(self, 
    ):
        """
        # Machine_states
        
        Stati della macchina a stati per la conversione dei record
        SMF 110 Subtype 1
        """
        super().__init__()
        
        self.INITIAL = 0                # Stato iniziale: non ho identificato alcun tipo di record
        self.RECORD_HEADER = 1          # Sono all'interno della sezione 
        self.HEADER_EXTENSION = 2       # Sono all'interno della sezione Header Extension
        self.SERVER_SECTION = 3         # Sono all'interno della sezione Server
        self.REQUEST_DATA_SECTION = 4   # Sono all'interno delle n sezioni dei dati veri e propri
        self.TRACKING_TOKEN = 5         # Il tracking Token è su due RIGHE. Quindi prendo la riga successiva

