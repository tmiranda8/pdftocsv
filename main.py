import sys, tabula, pandas, os
directory = os.getcwd()
slash = '\\'
default = 51

if len(sys.argv) > 1:
    pdf_name = sys.argv[1]
    path = fr'pdf\{pdf_name}.pdf'
    path = slash.join([directory, path])
    if len(sys.argv) > 3:
        csv_name = sys.argv[2]
        last_page = int(sys.argv[3])+1
        if len(sys.argv) > 4:
            last_page_length = int(sys.argv[4])
            if len(sys.argv) > 5:
                first_page_length = int(sys.argv[5])
            else:
                first_page_length = 27
        else:
            last_page_length = default
    else:
        csv_name = pdf_name
        first_page_length = 35
        last_page_length = default
        if len(sys.argv) == 2:
            last_page = 15
        else:
            last_page = int(sys.argv[2])+1
    output_path = fr'csv\{csv_name}.csv'
    output_path = slash.join([directory, output_path])
else:
    path = r'pdf\credicoop\test.pdf'
    output_path = r'csv\credicoop.csv'
    path = slash.join([directory, path])
    output_path = slash.join([directory, output_path])
    first_page_length = 35
    last_page_length = default
    last_page = 15

def page_call(i):
    if i == 1:
        page = tabula.read_pdf(path, pages=i, pandas_options={'header': None}, area=[first_page_length,0,91,100], relative_area=True, relative_columns=True, columns=[11,17,55,67,85,100])
    elif i == (last_page-1):
        page = tabula.read_pdf(path, pages=i, pandas_options={'header': None}, area=[24,0,last_page_length,100], relative_area=True, relative_columns=True, columns=[11,17,55,67,85,100])
    else:
        page = tabula.read_pdf(path, pages=i, pandas_options={'header': None}, area=[24,0,92,100], relative_area=True, relative_columns=True, columns=[11,17,55,67,85,100])
    page[0].columns = ['Fecha','ID','Descripcion','Debito','Credito','Saldo']
    return page

def to_list(df):
    DATA = {'Fecha':df[0]['Fecha'].values.tolist(),'ID':df[0]['ID'].values.tolist(),'Descripcion':df[0]['Descripcion'].values.tolist(),'Debito':df[0]['Debito'].values.tolist(),'Credito':df[0]['Credito'].values.tolist(),'Saldo':df[0]['Saldo'].values.tolist()}
    return DATA

def update(DATA,page):
    DATA['Fecha'].extend(page['Fecha'])
    DATA['ID'].extend(page['ID'])
    DATA['Descripcion'].extend(page['Descripcion'])
    DATA['Debito'].extend(page['Debito'])
    DATA['Credito'].extend(page['Credito'])
    DATA['Saldo'].extend(page['Saldo'])
    return DATA

def add_null_row(DATA):
    raw = [None]
    row = {}
    columns = ['Fecha','ID','Descripcion','Debito','Credito','Saldo']
    for i in range(0,6):
        row[columns[i]]=raw
    print(len(DATA['Fecha']))
    DATA = update(DATA,row)

def data_check(DATA):
    print (type(DATA))
    print(len(DATA.keys()))
    print(len(DATA['Fecha']))
    print(len(DATA['ID']))
    print(len(DATA['Descripcion']))
    print(len(DATA['Debito']))
    print(len(DATA['Credito']))
    print(len(DATA['Saldo']))

for i in range(1,last_page):
    if i == 1:
        page = page_call(i)
        DATA = to_list(page)
        add_null_row(DATA)
    else:
        page = page_call(i)
        add = to_list(page)
        DATA = update(DATA,add)
        add_null_row(DATA)
        if i == (last_page-1):
            dataframe = pandas.DataFrame.from_dict(DATA)
            dataframe.to_csv(path_or_buf=output_path, decimal=',')