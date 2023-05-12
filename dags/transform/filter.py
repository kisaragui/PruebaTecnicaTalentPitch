import pandas as pd
import json

def consigna(df):
      
      print("Applying query")
      try:   
            data =  pd.DataFrame.from_dict(json.loads(df), orient ='columns')
            query = data.groupby(["STNAME", "YEAR"])["AAWDT"].count()
            print(query)
            convert = query.reset_index().to_json(orient = 'columns')
            print("Total: {} registers grouped.".format(len(query))) 
      except:
            query = print("No se pudo leer el archivo")
      return convert

