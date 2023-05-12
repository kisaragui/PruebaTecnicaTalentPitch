import pandas as pd 
import os.path
import io
path = os.path.join(os.environ["AIRFLOW_HOME"],'dags','extraction')

def extract_csv_to_pandas(csv, **kwargs):
    try:
        ti = kwargs["ti"]
        print("Reading...")
        extraction = pd.read_csv('{}/{}'.format(path,csv))
        print("Reading... {} records ".format(len(extraction)))
        data = extraction.to_json(orient = 'columns')
        print("Reading csv in route:{}/{}.".format(path,csv))
    except: 
        data = print("File CSV not found")  
    return data
     
