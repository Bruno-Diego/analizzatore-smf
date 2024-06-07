import pandas as pd

class Export_excel(object):
    """
    # Export_excel
    
    Export di un dataframe in excel, con il blocco della prima
    riga e della prima colonna, con l'autofilter sulle colonne.
    Il datframe deve avere come prima riga i nomi delle colonne.
    """
    def __init__(self, 
    ):
        """
        # Export_excel
        
        Export di un dataframe in excel, con il blocco della prima
        riga e della prima colonna, con l'autofilter sulle colonne.
        Il datframe deve avere come prima riga i nomi delle colonne.
        """
        super().__init__()
        
        
    def export_excel(self,
        p_file_excel: str,
        p_df: pd.DataFrame,
        p_nome_sheet: str,
        p_nome_sheet2: str = None,
        p_df_2: str=None,
    ) -> None:
        
        writer = pd.ExcelWriter(p_file_excel)
        p_df.to_excel(writer,p_nome_sheet)

        # Freeze della prima riga
        _sheet = writer.book.active
        _sheet.freeze_panes = 'C2'
        _sheet.auto_filter.ref = _sheet.dimensions
        
        dims = {}
        for row in _sheet.rows:
            for cell in row:
                if cell.value:
                    # Massimo tra la dimensione della cella, e il 20% in puiù della
                    # dimensione del titolo (per tenere conto dell'autofilter)
                    dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
        for col, value in dims.items():
            _sheet.column_dimensions[col].width = value * 1.275
        
        if p_nome_sheet2 is not None and p_df_2 is not None:
            p_df_2.to_excel(writer, p_nome_sheet2)
            _sheet2 = writer.book.active
            _sheet2 = writer.sheets[p_nome_sheet2]
            _sheet2.freeze_panes = 'A2'
            _sheet2.auto_filter.ref = _sheet2.dimensions
            
            dims_2 = {}
            for row_2 in _sheet2.rows:
                for cell_2 in row_2:
                    if cell_2.value:
                        # Massimo tra la dimensione della cella, e il 20% in puiù della
                        # dimensione del titolo (per tenere conto dell'autofilter)
                        dims_2[cell_2.column_letter] = max((dims_2.get(cell_2.column_letter, 0), len(str(cell_2.value))))
            for col_2, value_2 in dims_2.items():
                _sheet2.column_dimensions[col_2].width = value_2 * 1.3
        # Chiusura del file
        writer.close()
        # Return the Excel writer
        
        return writer