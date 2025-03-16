from libs.vars import toolkit

def updater(dict, value) -> dict:
    for label in toolkit.labels:
        dict[label].extend(value[label])
    return dict

def null_row(dict) -> None:
    raw = [None]
    line = {}
    for label in toolkit.labels:
        line[label]=raw
    updater(dict, line)

def trace():
    ...