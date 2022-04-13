import airflow
import datetime as dt
from hes_scripts.common_package.scraper import scrape_listings_to_pickle,\
    clean_listings_from_pickle_to_pickle
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 4, 12, 00, 00, 00, 00),
    'concurrency': 1,
    'retries': 1,
    'schedule_interval': '@daily'
}

raw_data_path = '/opt/airflow/raw_data/'
city = 'Portland, OR'
raw_filepath = raw_data_path + city + '_raw' + '.pickle'
clean_filepath = raw_data_path + city + '_clean' + '.pickle'

def scrape_data():
    scrape_listings_to_pickle(raw_filepath)

def clean_data():
    clean_listings_from_pickle_to_pickle(raw_filepath, clean_filepath)

etl_dag = DAG('etl_dag', catchup=False, default_args=default_args)
opr_scrape_data = PythonOperator(task_id='scrape', python_callable=scrape_listings_to_pickle,\
    dag=etl_dag)
opr_clean_data = PythonOperator(task_id='clean', python_callable=clean_listings_from_pickle_to_pickle,\
    dag=etl_dag)


opr_scrape_data >> opr_clean_data


