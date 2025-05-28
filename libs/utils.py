import pandas
from libs.vars import toolkit, files, tracer
from libs.menu import output_console

def updater(dict, value) -> dict:
    for label in toolkit.labels:
        dict[label].extend(value[label])
    return dict

def to_list(dataframe) -> dict:
    return {label:dataframe[label].values.tolist() for label in toolkit.labels}

def to_df(data) -> pandas.DataFrame:
    return pandas.DataFrame.from_dict(data)

def drop_nan(dataframe) -> None:
    dataframe.dropna(subset=['Fecha'],inplace=True)

def format(dataframe) -> pandas.DataFrame:
    for label in tracer.labels:
        if label in toolkit.labels:
            dataframe[label] = dataframe[label].astype(str).str.replace('$','', regex=False)
            dataframe[label] = dataframe[label].astype(str).str.replace('.','', regex=False)
            dataframe[label] = dataframe[label].astype(str).str.replace(',','.', regex=False)
            dataframe[label] = pandas.to_numeric(dataframe[label], errors='coerce')
    return dataframe.reset_index(drop=True)

def pipeline(dataframe) -> pandas.DataFrame:
    drop_nan(dataframe)
    return format(dataframe)

def csv_export(dataframe) -> None: 
    output_console()
    dataframe.to_csv(path_or_buf=files.output_path)
