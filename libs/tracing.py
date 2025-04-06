import pandas
from libs.vars import tracer, results
from libs.utils import pipeline
from rich import print as rprint

def tracer_dataset(dataframe, i) -> dict:
    dataset = {}
    dataset.update({'current_first':tracer.set_current_first(dataframe)})
    dataset.update({'current_last':{label:dataframe.iloc[-1][label] for label in tracer.labels}})
    if i == 1:
        dataset.update({'previous_last':{label:dataframe.iloc[0][label] for label in tracer.labels}})
        dataset.update({'current_first':{label:dataframe.iloc[1][label] for label in tracer.labels}})
    return dataset

def trace() -> float:
    saldo = tracer.previous_last['Saldo']
    proximo_saldo = tracer.current_first['Saldo']
    for label in tracer.find:
        if pandas.notna(tracer.current_first[label]):
            operacion = tracer.current_first[label]
    error = round(float((saldo + operacion) - proximo_saldo), 2)
    return abs(error) if abs(error) < 1e-2 else error

def validator(dataframe, i) -> None:
    pipeline(dataframe)
    dataset = tracer_dataset(dataframe, i)
    tracer.set_tracer(dataset)
    results.set_results(i, dataframe.shape[0], trace())