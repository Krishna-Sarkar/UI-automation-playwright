import pandas as pd
import os
import configparser

def read_xls(file_name:str, sheet_name:str):
    file_path = f'{os.curdir}/testdata/{file_name}'
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return [tuple(row) for row in df.to_numpy()]

def read_config():
    config = configparser.ConfigParser()
    config.read(os.getcwd()+'/'+'config.ini')
    return config