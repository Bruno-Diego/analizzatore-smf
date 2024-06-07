class Messages(object):
    """
    # Messages
    
    Classe con i messaggi di errore dell'applicazione
    """
    def __init__(self, 
    ):
        """
        # Messages
        
        Classe con i messaggi di errore dell'applicazione
        """
        super().__init__()
        
    def SMFF_0001_RECORD_SMF_NO_123(self,
        p_oggetto: str,
        p_function: str,
        p_nomfile: str,
    ) -> str:
        return f'SMFF_0001: {p_oggetto}.{p_function} IL file {p_nomfile} non è nel formato SMF123 Subtype 2: non è stato possibile trovare la riga '
    
    def SMFF_0001_RECORD_SMF_NO_123(self,
        p_oggetto: str,
        p_function: str,
        p_nomfile: str,
        p_field_name: str,
        p_field_val
    ) -> str:
        return f'SMFF-0001: {p_oggetto}.{p_function} - Formato file {p_nomfile} non corretto: Il campo {p_field_name} non ha il valore {p_field_val}.'
    
    def SMFF_0002_HEADERS_MANCANTI(self,
        p_oggetto: str,
        p_function: str,
        p_nomfile: str,
        p_header: str,                                   
    ) -> str:
        return f'SMFF-00002: {p_oggetto}.{p_function} - Formato file {p_nomfile} non corretto: Manca header {p_header}'