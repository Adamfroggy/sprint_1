import pandas as pd

def null_count(df):
    return df.isnull().sum().sum()