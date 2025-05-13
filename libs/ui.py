import os
from libs.interface import StringPrompt, IntegerPrompt
from libs.modes import templates
from rich import print as rprint

def ask_mode() -> StringPrompt:
    mode = StringPrompt.ask(
        'Modo', 
        choices=list(templates.keys()),
        case_sensitive=False,
        default=list(templates.keys())[3])
    return mode

def ask_pdf_name() -> StringPrompt:
    pdf_name = StringPrompt.ask(
        'Ingrese [bold underline red]el nombre exacto[/bold underline red] del archivo PDF',
        default='test'
        )
    return pdf_name

def file_exists(mode, pdf_name) -> bool:
    pdf_path = rf'pdf\{mode}\{pdf_name}.pdf'
    if os.path.exists(pdf_path):
        templates[mode]['path']=pdf_path
        templates[mode]['output_path']=rf'csv\{mode}\{pdf_name}.csv'
        return True
    else:
        rprint(fr"[bold red]Error:[/bold red] '{pdf_name}' no existe en /pdf/{mode}/")
        rprint('Intente de nuevo. Asegurese de que el archivo este ubicado en el directorio correcto')
        return False

def ask_pages(mode) -> bool:
    pages = IntegerPrompt.ask(
    'Cantidad de paginas',
    default=templates[mode]['pages'])
    if 0 < pages < 4000:
        templates[mode]['pages'] = pages
        return True
    else:
        rprint(f'Ingreso un número invalido ({pages}). Debe ingresar un numero entero entre 0 y 100')
        return False

def ask_last_page_length(mode) -> IntegerPrompt:
    last_page_length = IntegerPrompt.ask(
    'Longitud de tabla en ultima pagina',
    default=templates[mode]['last_page_length']
    )
    return last_page_length

def length_within_area(mode, last_page_length) -> bool:
    if templates[mode]['area'][0] < last_page_length < templates[mode]['area'][2]:
        templates[mode]['last_page_length'] = last_page_length
        return True
    else:
        rprint(f"Ingreso un número invalido ({last_page_length}). Debe ingresar un numero entero entre {templates[mode]['area'][0]} y {templates[mode]['area'][2]}")
        return False