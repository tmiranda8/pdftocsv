import sys, os
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
            cls._instance.path = dir(r'pdf\credicoop\test.pdf')
            cls._instance.output_path = dir(r'csv\credicoop\credicoop.csv')
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
            cls._instance.first_page_length = 35
            cls._instance.last_page_length = 51
            cls._instance.last_page = 15
        return cls._instance
    @classmethod
    def set_mode(cls, mode):
        instance = cls._instance
        if mode in libs.modes.templates:
            instance.area = libs.modes.templates[mode]['area']
            instance.columns = libs.modes.templates[mode]['columns']
            instance.labels = libs.modes.templates[mode]['labels']
        else:
            raise ValueError(f'{mode} es un modo invalido. intente nuevamente')
    def set_custom(cls, area, columns):
        ...
toolkit = Mode()