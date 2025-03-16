import pandas
from libs.vars import files

def csv_export(data) -> None: 
    dataframe = pandas.DataFrame.from_dict(data)
    dataframe.to_csv(path_or_buf=files.output_path, decimal=',')