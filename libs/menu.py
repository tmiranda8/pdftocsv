from rich import box, print as rprint
from rich.console import Console
from rich.table import Table
from libs import ui
from libs.modes import templates
from libs.vars import toolkit, results

def input_handler() -> str:
    while True:
        mode = ui.ask_mode()
        if mode in templates:
            while True:
                pdf_name = ui.ask_pdf_name()
                if ui.file_exists(mode, pdf_name):
                    break
            while True:
                if ui.ask_pages(mode):
                    break
            while True:
                last_page_length = ui.ask_last_page_length(mode)
                if ui.length_within_area(mode, last_page_length):
                    break
            return mode
        else:
            rprint('Ha ocurrido un problema. Contacte al administrador')

def output_console():
    console = Console()
    table = Table(box=box.MINIMAL_DOUBLE_HEAD, )
    table.add_column('Pagina',justify='center',style='grey70')
    table.add_column('Indice ultima linea',justify='center',style='cyan')
    table.add_column('Error en saldo',justify='center',style='green4')
    table.add_column('Saldo pag. anterior',justify='center',style='bright_white')
    table.add_column('Movimiento',justify='center',style='bright_white')
    table.add_column('Saldo pag. actual',justify='center',style='bright_white')
    for i in range(0,toolkit.pages):
        table.add_row(*(str(getattr(results, attr)[i]) for attr in vars(results)))
    console.print(table)