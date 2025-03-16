from rich import pretty, traceback
traceback.install()
from libs.export import csv_export
from libs.menu import input_handler
from libs.parser import parse
from libs.utils import updater
from libs.vars import toolkit

def main() -> None:
    mode = input_handler()
    toolkit.set_mode(mode)
    for i in range(1,toolkit.pages):
        if i > 1:
            dict = updater(dict, parse(i))
            if i == (toolkit.pages-1):
                csv_export(dict)
                
        else:
            dict = parse(i)
        pretty.pprint(len(dict['Fecha']))


if __name__ == "__main__":
    main()