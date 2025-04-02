from rich import traceback
traceback.install()

from libs.menu import input_handler
from libs.parser import parse
from libs.utils import updater, pipeline, to_df, csv_export
from libs.vars import toolkit


def main() -> None:
    mode = input_handler()
    toolkit.set_mode(mode)
    for i in range(1,toolkit.pages+1):
        if i > 1:
            data = updater(data, parse(i))
            if i == (toolkit.pages):
                dataframe = to_df(data)
                csv_export(pipeline(dataframe))
        else:
            data = parse(i)

if __name__ == "__main__":
    main()