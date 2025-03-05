import tabula
from libs.utils import null_row
from libs.vars import files, toolkit

def parse(i):
    
    if i == 1:
        first = toolkit.area.copy()
        first[0] = toolkit.first_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=first, relative_area=True, relative_columns=True, columns=toolkit.columns)
    elif i == (toolkit.last_page-1):
        last = toolkit.area.copy()
        last[2] = toolkit.last_page_length
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=last, relative_area=True, relative_columns=True, columns=toolkit.columns)
    else:
        dataframe = tabula.read_pdf(files.path, pages=i, pandas_options={'header': None}, area=toolkit.area, relative_area=True, relative_columns=True, columns=toolkit.columns)
    
    dataframe[0].columns = toolkit.labels
    dict = {'Fecha':dataframe[0]['Fecha'].values.tolist(),'ID':dataframe[0]['ID'].values.tolist(),'Descripcion':dataframe[0]['Descripcion'].values.tolist(),'Debito':dataframe[0]['Debito'].values.tolist(),'Credito':dataframe[0]['Credito'].values.tolist(),'Saldo':dataframe[0]['Saldo'].values.tolist()}
    null_row(dict)
    return dict

