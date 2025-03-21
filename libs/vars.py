import os, pandas
import libs.modes

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
    def set_path(cls, path, dir):
        instance = cls._instance
        setattr(instance, path, dir)
files = Paths()

class Mode():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.area = None
            cls._instance.columns = None
            cls._instance.labels = None
            cls._instance.pages = None
            cls._instance.first_page_length = None
            cls._instance.last_page_length = None
        return cls._instance
    @classmethod
    def set_mode(cls, mode):
        instance = cls._instance
        if mode in libs.modes.templates:
            for key, value in libs.modes.templates[mode].items():
                if hasattr(instance,key):
                    setattr(instance,key,value)
                elif hasattr(files, key):
                    files.set_path(key,value)
        else:
            raise ValueError(f'{mode} es un modo invalido. intente nuevamente')
toolkit = Mode()

class Tracer():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.labels = ['Credito','Debito','Saldo']
            cls._instance.find = ['Credito','Debito']
            cls._instance.tracers = ['previous_last','current_first','current_last']
            cls._instance.previous_last = None
            cls._instance.current_first = None
            cls._instance.current_last = None
        return cls._instance
    @classmethod
    def set_tracer(cls, dataset):
        instance = cls._instance
        for key, value in dataset.items():
            if hasattr(instance,key):
                setattr(instance,key,value)
tracer = Tracer()

class Results():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.page = []
            cls._instance.endofpage_index = []
            cls._instance.error = []
            cls._instance.previous_total = []
            cls._instance.current_transaction = []
            cls._instance.current_total = []
        return cls._instance
    @classmethod
    def set_results(cls, page, index, error):
        instance = cls._instance
        instance.page.append(page)
        last_index = instance.endofpage_index[-1] if instance.endofpage_index else -1
        new_index = index + last_index
        instance.endofpage_index.append(new_index)
        instance.error.append(error)
        if tracer.current_first is not None:
            instance.previous_total.append(tracer.previous_last['Saldo'])
            instance.current_total.append(tracer.current_first['Saldo'])
            for label in tracer.find:
                if pandas.notna(tracer.current_first[label]):
                    instance.current_transaction.append(tracer.current_first[label])
            tracer.set_tracer({'previous_last':tracer.current_last})
        else:
            instance.previous_total.append(float(0))
            instance.current_total.append(tracer.previous_last['Saldo'])
            for label in tracer.find:
                if pandas.notna(tracer.previous_last[label]):
                    instance.current_transaction.append(tracer.previous_last[label])
results = Results()