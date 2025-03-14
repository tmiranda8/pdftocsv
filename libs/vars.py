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
files = Paths()

class Mode():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.area = None
            cls._instance.columns = None
            cls._instance.labels = None
            cls._instance.first_page_length = None
            cls._instance.last_page_length = None
            cls._instance.pages = None
        return cls._instance
    @classmethod
    def set_mode(cls, mode):
        instance = cls._instance
        if mode in libs.modes.templates:
            for key, value in libs.modes.templates[mode].items():
                if hasattr(instance,key):
                    setattr(instance,key,value)
            for key, value in libs.modes.templates[mode].items():
                if hasattr(files,key):
                    setattr(files, key, dir(libs.modes.templates[mode][key]))
        else:
            raise ValueError(f'{mode} es un modo invalido. intente nuevamente')
toolkit = Mode()