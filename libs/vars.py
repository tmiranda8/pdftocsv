import os
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
            cls._instance.results = [[],[],[]]
        return cls._instance
    @classmethod
    def set_tracer(cls, dataset):
        instance = cls._instance
        for key, value in dataset.items():
            if hasattr(instance,key):
                setattr(instance,key,value)
tracer = Tracer()