import tabula, warnings
from libs.utils import to_list
from libs.tracing import validator
from libs.vars import files, toolkit
from rich import print as rprint

def parse(i) -> dict:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        if i == 1:
            first = toolkit.area.copy()
            first[0] = toolkit.first_page_length
            if i == (toolkit.pages):
                first[2] = toolkit.last_page_length
            dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=first, relative_area=True, relative_columns=True, columns=toolkit.columns)
        elif i == (toolkit.pages):
            last = toolkit.area.copy()
            last[2] = toolkit.last_page_length
            dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=last, relative_area=True, relative_columns=True, columns=toolkit.columns)
        else:
            dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=toolkit.area, relative_area=True, relative_columns=True, columns=toolkit.columns)
        dataframe[0].columns = toolkit.labels
        data = to_list(dataframe[0])
        # rprint(data)
        validator(dataframe[0], i)
    return data
