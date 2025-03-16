import os
from rich import print as rprint
from libs.interface import StringPrompt, IntegerPrompt
from libs.modes import templates

def input_handler() -> str:
    while True:
        mode = StringPrompt.ask(
            'Modo', 
            choices=list(templates.keys()),
            case_sensitive=False,
            default=list(templates.keys())[1])
        if mode in templates:
            settings = templates[mode]
            while True:
                pdf_name = StringPrompt.ask(
                'Ingrese [bold underline red]el nombre exacto[/bold underline red] del archivo PDF',
                default='test'
                )
                pdf_path = rf'pdf\{mode}\{pdf_name}.pdf'
                if os.path.exists(pdf_path):
                    settings['path']=pdf_path
                    settings['output_path']=rf'csv\{mode}\{pdf_name}.csv'
                    break
                else:
                    rprint(fr"[bold red]Error:[/bold red] '{pdf_name}' no existe en /pdftocsv/{mode}/")
                    rprint('Intente de nuevo. Asegurese de que el archivo este ubicado en el directorio correcto')
            while True:
                pages = IntegerPrompt.ask(
                    'Cantidad de paginas',
                    default=templates[mode]['pages']
                )
                if 0 < pages < 100:
                    settings['pages'] = pages
                    break
                else:
                    rprint(f'Ingreso un número invalido ({pages}). Debe ingresar un numero entero entre 0 y 100')
            while True:
                last_page_length = IntegerPrompt.ask(
                    'Longitud de tabla en ultima pagina',
                    default=templates[mode]['last_page_length']
                )
                if settings['area'][0] < last_page_length < settings['area'][2]:
                    settings['last_page_length'] = last_page_length
                    break
                else:
                    rprint(f"Ingreso un número invalido ({last_page_length}). Debe ingresar un numero entero entre {settings['area'][0]} y {settings['area'][2]}")
            return mode
        else:
            rprint('Ha ocurrido un problema. Contacte al administrador')