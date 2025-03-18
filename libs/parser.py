import tabula
from libs.utils import validator, to_list
from libs.vars import files, toolkit

def parse(i) -> dict:
    if i == 1:
        first = toolkit.area.copy()
        first[0] = toolkit.first_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=first, relative_area=True, relative_columns=True, columns=toolkit.columns)
    elif i == (toolkit.pages):
        last = toolkit.area.copy()
        last[2] = toolkit.last_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=last, relative_area=True, relative_columns=True, columns=toolkit.columns)
    else:
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=toolkit.area, relative_area=True, relative_columns=True, columns=toolkit.columns)
    dataframe[0].columns = toolkit.labels
    data = to_list(dataframe[0])
    validator(dataframe[0], i)
    return data
