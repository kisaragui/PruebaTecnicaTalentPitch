import pandas as pd
import json

def detect_missing_values(df):
    try:
        data = pd.DataFrame.from_dict(json.loads(df), orient ='columns')
        print("Detecting misses values in the data...")
        detect = data.isna().sum().sum()
        print("Total {} missing values".format(detect))
        convert = data.to_json(orient = 'columns')
    except:
        dectect = print("The CSV can not reading")    
    return convert

def drop_missing_values(df):
    try:
        data_raw =  pd.DataFrame.from_dict(json.loads(df), orient ='columns')
        print("Removing missing valuess....")
        data_cleaned= data_raw.dropna()
        number_removed = len(data_raw) - len(data_cleaned)
        print("Total: {} registers removed.".format(number_removed))
        convert = data_cleaned.to_json(orient = 'columns')
    except:
        clean = print("The CSV can not reading") 
    return convert

