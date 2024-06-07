import click
from colorama import Fore, Back, Style

class Help_print(object):
    """
    # Help_print
    
    Stampa con click l'help
    """
    def __init__(self, 
    ):
        """
        # Help_print
        
        Stampa con click l'help
        """
        super().__init__()


    def show_help(self):
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
        
    def show_changelog(self, p_changelog):
        print(p_changelog)
            
    def print_error(self, p_error: str):
        print(Fore.RED + f' ERRORE : {p_error}')
        print(Style.RESET_ALL)
        
    def print_warn(self, p_warn: str):
        print(Fore.YELLOW + f' WARNING : {p_warn}')
        print(Style.RESET_ALL)
        
    def print_info(self, p_info: str):
        print(Fore.GREEN + f'INFO : {p_info}')
        print(Style.RESET_ALL)
