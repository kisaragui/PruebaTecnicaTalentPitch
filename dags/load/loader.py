import time
import pandas as pd
import json
import os.path
import csv as c

path = os.path.join(os.environ["AIRFLOW_HOME"],'dags','load')

def write_new_csv(df, csv):
    try:
        data = pd.DataFrame.from_dict(json.loads(df), orient ='columns')
        date = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        csvname = '{}/{}_{}.csv'.format(path,csv, date)
        convert = data.to_csv(csvname, quoting=c.QUOTE_NONNUMERIC, index=False)
        print("Loading new csv in route:{}".format(csvname))
    except:
       convert = print("The CSV can not reading") 
    return convert