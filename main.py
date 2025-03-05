from rich import pretty, traceback
traceback.install()
from lib.vars import toolkit
from lib.parser import parse
from lib.utils import updater
from lib.export import csv_export
from lib.interface import StringPrompt, IntegerPrompt
from lib.modes import templates

def main() -> None:
    while True:
        result = StringPrompt.ask('indique el modo', choices=list(templates.keys()), default=list(templates.keys())[1])
        if result in templates:
            toolkit.set_mode(result)
            break
    # while True:
    #     result = IntegerPrompt
    for i in range(1,toolkit.last_page):
        if i > 1:
            dict = updater(dict, parse(i))
            if i == (toolkit.last_page-1):
                csv_export(dict)
        else:
            dict = parse(i)
        pretty.pprint(len(dict['Fecha']))


if __name__ == "__main__":
    main()