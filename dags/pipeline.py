import pandas as pd
import extraction.read as e
import transform.clean as t
import load.loader as l
import transform.filter as f 
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

dag = DAG(dag_id='etl_process', 
          default_args = {
            'owner': 'airflow',
            'depends_on_past': False,
            'retry_delay': timedelta(minutes=5),
            "start_date": datetime(2022,5,12),
            },
          catchup = False,
          schedule_interval= '0 0 * * *')

extraction_task = PythonOperator(task_id='read_csv',
                          python_callable=e.extract_csv_to_pandas,
                          op_kwargs ={'csv':'Traffic_Flow_Map_Volumes.csv'},
                          dag=dag, 
                          show_return_value_in_logs = True)

detect_task = PythonOperator(task_id='detect_missing_values',
                          python_callable=t.detect_missing_values,
                          op_kwargs={'df':"{{ ti.xcom_pull(task_ids='read_csv') }}"},
                          dag=dag,
                          show_return_value_in_logs = True)

clean_task = PythonOperator(task_id='drop_missing_values',
                          python_callable=t.drop_missing_values,
                          op_kwargs={'df':"{{ ti.xcom_pull(task_ids='detect_missing_values') }}"},
                          dag=dag,
                          show_return_value_in_logs = True)

filter_task = PythonOperator(task_id='filter_query',
                          python_callable=f.consigna,
                          op_kwargs={'df':"{{ ti.xcom_pull(task_ids='drop_missing_values') }}"},
                          dag=dag,
                          show_return_value_in_logs = True)

load_task = PythonOperator(task_id='load_new_csv',
                          python_callable=l.write_new_csv,
                          op_kwargs={'df':"{{ ti.xcom_pull(task_ids='filter_query') }}",
                                     "csv": "Total_traffic_grouped"},
                          dag=dag,
                          show_return_value_in_logs = True)


extraction_task >> detect_task >> clean_task >> filter_task >> load_task


                                    
