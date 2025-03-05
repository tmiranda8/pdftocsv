import sys

def updater(dict, value) -> dict:
    dict['Fecha'].extend(value['Fecha'])
    dict['ID'].extend(value['ID'])
    dict['Descripcion'].extend(value['Descripcion'])
    dict['Debito'].extend(value['Debito'])
    dict['Credito'].extend(value['Credito'])
    dict['Saldo'].extend(value['Saldo'])
    return dict

def null_row(dict) -> None:
    raw = [None]
    line = {}
    columns = ['Fecha','ID','Descripcion','Debito','Credito','Saldo']
    for i in range(0,6):
        line[columns[i]]=raw
    dict = updater(dict, line)

def handler():
    ...