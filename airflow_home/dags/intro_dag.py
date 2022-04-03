import airflow


import datetime as dt

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 4, 2, 9, 10, 00, 00),
    'concurrency': 1,
    'retries': 0
}

from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def scraper():
    print("hello from python scraper")

def clean_data():
    print("hello from clean data") 

simple_dag = DAG('simple_dag', catchup=False, default_args=default_args, schedule_interval='*/1 * * * *')

opr_start = BashOperator(task_id='start',\
    bash_command='echo "Hi! start scraping of home listings"',\
        dag=simple_dag)
opr_scraper = PythonOperator(task_id='scrape', python_callable=scraper,\
    dag=simple_dag)
opr_clean = PythonOperator(task_id='clean_data', python_callable=clean_data,\
    dag=simple_dag)
opr_stop = BashOperator(task_id='stop',\
    bash_command='echo "bye! scraped all the data"', dag=simple_dag)

opr_start >> opr_scraper >> opr_clean >> opr_stop