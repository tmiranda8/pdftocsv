import os, pandas
import libs.modes
from rich import print as rprint

def dir(path) -> str:
    slash = '\\'
    directory = os.getcwd()
    return slash.join([directory, path])

class Paths():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.path = ''
            cls._instance.output_path = ''
        return cls._instance
    @classmethod
    def verify_directory(cls):
        for file in ["pdf", "csv"]:
            for mode in libs.modes.templates:
                path = os.path.join(file, mode)
                os.makedirs(path, exist_ok=True)
    @classmethod
    def set_path(cls, path, dir):
        instance = cls._instance
        setattr(instance, path, dir)
files = Paths()
files.verify_directory()

class Mode():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            for attr in ['mode','area','columns','labels','pages','first_page_length','last_page_length']:
                setattr(cls._instance, attr, None)
        return cls._instance
    @classmethod
    def set_mode(cls, mode):
        instance = cls._instance
        if mode in libs.modes.templates:
            setattr(instance, 'mode', mode)
            for key, value in libs.modes.templates[mode].items():
                if hasattr(instance,key):
                    setattr(instance,key,value)
                elif hasattr(files, key):
                    files.set_path(key,value)
            tracer.set_tracer_labels()
        else:
            raise ValueError(f'{mode} es un modo invalido. intente nuevamente')
toolkit = Mode()

class Tracer():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tracers = ['previous_last','current_first','current_last']
            for attr in cls._instance.tracers + ['labels', 'find']:
                setattr(cls._instance, attr, None)
        return cls._instance
    @classmethod
    def set_tracer(cls, dataset):
        instance = cls._instance
        for key, value in dataset.items():
            if hasattr(instance,key):
                setattr(instance,key,value)
    @classmethod
    def set_tracer_labels(cls):
        instance = cls._instance
        mode_labels = []
        find = []
        for label in toolkit.labels:
            if label in ['Credito','Debito','Importe','Saldo']:
                mode_labels.append(label)
            if label in ['Credito','Debito','Importe']:
                find.append(label)
        instance.set_tracer({'labels':mode_labels,'find':find})
    @classmethod
    def set_current_first(cls, dataframe):
        row_index = 0
        while row_index < len(dataframe):
            first_row = dataframe.iloc[row_index]
            if pandas.notna(first_row.get('Saldo')) and any(pandas.notna(first_row.get(label)) for label in tracer.find):
                return {label:dataframe.iloc[row_index][label] for label in cls._instance.labels}
            row_index += 1
tracer = Tracer()

class Results():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            for attr in ['page','endofpage_index','error','previous_total','current_transaction','current_total']:
                setattr(cls._instance, attr, [])
        return cls._instance
    @classmethod
    def set_results(cls, page, index, error):
        instance = cls._instance
        instance.page.append(page)
        instance.endofpage_index.append(instance.set_index(index))
        instance.error.append(error)
        instance.previous_total.append(tracer.previous_last['Saldo'])
        instance.current_total.append(tracer.current_first['Saldo'])
        for label in tracer.find:
            if pandas.notna(tracer.current_first[label]):
                instance.current_transaction.append(tracer.current_first[label])
        tracer.set_tracer({'previous_last':tracer.current_last})
    @classmethod
    def set_index(cls, index):
        last_index = cls._instance.endofpage_index[-1] if cls._instance.endofpage_index else -1
        new_index = index + last_index
        return new_index
results = Results()