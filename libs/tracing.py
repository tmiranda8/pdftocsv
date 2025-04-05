import pandas
from libs.vars import tracer, results
from libs.utils import pipeline

def tracer_dataset(dataframe, i) -> dict:
    dataset = {}
    if i == 1:
        dataset.update({'previous_last':{label:dataframe.iloc[-1][label] for label in tracer.labels}})
    else:
        index = 0
        while index < len(dataframe):
            fr = dataframe.iloc[index]
            if pandas.notna(fr['Saldo']) and (pandas.notna(['Credito']) or pandas.notna(['Debito'])):
                dataset.update({'current_first':{label:dataframe.iloc[index][label] for label in tracer.labels}})
                break
            index += 1
        dataset.update({'current_last':{label:dataframe.iloc[-1][label] for label in tracer.labels}})
    return dataset

def trace() -> float:
    if tracer.current_first is not None:
        saldo = tracer.previous_last['Saldo']
        proximo_saldo = tracer.current_first['Saldo']
        for label in tracer.find:
            if pandas.notna(tracer.current_first[label]):
                operacion = tracer.current_first[label]
        error = round(float((saldo + operacion) - proximo_saldo), 2)
        return abs(error) if abs(error) < 1e-2 else error
    else:
        return float(0)

def validator(dataframe, i) -> None:
    pipeline(dataframe)
    dataset = tracer_dataset(dataframe, i)
    tracer.set_tracer(dataset)
    results.set_results(i, dataframe.shape[0], trace())