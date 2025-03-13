import tabula
from libs.utils import null_row
from libs.vars import files, toolkit

dict = dict()

def parse(i):
    if i == 1:
        first = toolkit.area.copy()
        first[0] = toolkit.first_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=first, relative_area=True, relative_columns=True, columns=toolkit.columns)
    elif i == (toolkit.pages-1):
        last = toolkit.area.copy()
        last[2] = toolkit.last_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=last, relative_area=True, relative_columns=True, columns=toolkit.columns)
    else:
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=toolkit.area, relative_area=True, relative_columns=True, columns=toolkit.columns)
    dataframe[0].columns = toolkit.labels
    dict = {label:dataframe[0][label].values.tolist() for label in toolkit.labels}
    null_row(dict)
    return dict

