import pandas as pd
import os


def read(file):
    dir = os.getcwd()
    data = pd.read_csv(dir+file, encoding='latin1')
    return(data)
