import pandas, warnings
from libs.vars import toolkit, files, tracer, results
from libs.menu import output_console
from rich import pretty


def updater(dict, value) -> dict:
    for label in toolkit.labels:
        dict[label].extend(value[label])
    return dict

def drop_nan(dataframe) -> None:
    dataframe.dropna(subset=['Fecha'],inplace=True)

def format(dataframe) -> pandas.DataFrame:
    for label in tracer.labels:
        if label in toolkit.labels:
            dataframe[label] = dataframe[label].astype(str).str.replace('.','', regex=False)
            dataframe[label] = dataframe[label].astype(str).str.replace(',','.', regex=False)
            dataframe[label] = pandas.to_numeric(dataframe[label], errors='coerce')
    return dataframe.reset_index(drop=True)

def pipeline(dataframe) -> pandas.DataFrame:
    drop_nan(dataframe)
    dataframe = format(dataframe)
    # pretty.pprint(dataframe)
    # pretty.pprint(tracer.results)
    return dataframe

def tracer_dataset(dataframe, i) -> dict:
    dataset = {}
    if i == 1:
        dataset.update({'previous_last':{label:dataframe.iloc[-1][label] for label in tracer.labels}})
    else:
        dataset.update({'current_first':{label:dataframe.iloc[0][label] for label in tracer.labels}})
        dataset.update({'current_last':{label:dataframe.iloc[-1][label] for label in tracer.labels}})
    return dataset

def trace():
    if tracer.current_first is not None:
        saldo = tracer.previous_last['Saldo']
        proximo_saldo = tracer.current_first['Saldo']
        for label in tracer.find:
            if pandas.notna(tracer.current_first[label]):
                operacion = tracer.current_first[label]
        error = float((saldo + operacion) - proximo_saldo)
        tracer.set_tracer({'previous_last':tracer.current_last})
        return error
    else:
        return float(0)

def validator(dataframe, i):
    pipeline(dataframe)
    dataset = tracer_dataset(dataframe, i)
    tracer.set_tracer(dataset)
    # export_results(i, dataframe.shape[0], trace())
    results.set_results(i, dataframe.shape[0], trace())

# def export_results(page, lines, error):
#     current = [[page], [lines], [error]]
#     stored_data = [[],[],[]]
#     for i in range(0,3):
#         if i == 1:
#             if page > 1:
#                 pretty.pprint(tracer.results[i])
#                 pretty.pprint(current[i])
#                 stored_data[i] = tracer.results[i] + current[i]
#                 pretty.pprint(stored_data[i])
#             else:
#                 stored_data[i].extend(current[i])
#         else:
#             stored_data[i] = tracer.results[i]
#             stored_data[i].extend(current[i])
#     tracer.set_tracer({'results':stored_data})

def to_list(dataframe) -> dict:
    return {label:dataframe[label].values.tolist() for label in toolkit.labels}

def to_df(data) -> pandas.DataFrame:
    return pandas.DataFrame.from_dict(data)

def csv_export(dataframe) -> None: 
    output_console()
    dataframe.to_csv(path_or_buf=files.output_path)
