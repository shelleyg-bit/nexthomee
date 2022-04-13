from hes_scripts.common_package.scraper import scrape_listings_to_pickle,\
    clean_listings_from_pickle_to_pickle


def scrape_data():
    scrape_listings_to_pickle(city, raw_filepath)

def clean_data():
    clean_listings_from_pickle_to_pickle(raw_filepath, clean_filepath)

def main():
    import pickle
    import pandas as pd

    scrape_data()
    clean_data()
    
    with open(clean_filepath, 'rb') as f:
        portland_listings = pickle.load(f)
    pd.set_option('display.max_columns', 20)
    print(portland_listings)


if __name__ == "__main__":
    import os
    from pathlib import Path
    currpath = os.getcwd()
    raw_data_path = f'{currpath}/test_runs/'
    if not os.path.exists(raw_data_path):
        os.mkdir(raw_data_path)
    city = 'Portland, OR'
    raw_filepath = raw_data_path + city + '_raw' + '.pickle'
    clean_filepath = raw_data_path + city + '_clean' + '.pickle'
    main()
else:
    import airflow
    import datetime as dt
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    raw_data_path = '/opt/airflow/raw_data/'
    city = 'Portland, OR'
    raw_filepath = raw_data_path + city + '_raw' + '.pickle'
    clean_filepath = raw_data_path + city + '_clean' + '.pickle'

    default_args = {
        'owner': 'airflow',
        'start_date': dt.datetime(2022, 4, 12, 00, 00, 00, 00),
        'concurrency': 1,
        'retries': 1,
        'schedule_interval': '@daily'
    }

    etl_dag = DAG('etl_dag', catchup=False, default_args=default_args)
    opr_scrape_data = PythonOperator(task_id='scrape', python_callable=scrape_data,\
        dag=etl_dag)
    opr_clean_data = PythonOperator(task_id='clean', python_callable=clean_data,\
        dag=etl_dag)


    opr_scrape_data >> opr_clean_data

