from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/scripts')

from extract_weather import extract_data
from load_to_postgres import load_data

default_args = {
    'owner': 'admin',
    'start_date': datetime(2025, 1, 1)
}

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule='@hourly',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_weather',
        python_callable=extract_data
    )

    transform_task = SparkSubmitOperator(
        task_id='transform_weather',
        application='/opt/airflow/spark/transform_weather.py',
        conn_id='spark_default'
    )

    load_task = PythonOperator(
        task_id='load_postgres',
        python_callable=load_data
    )

    extract_task >> transform_task >> load_task