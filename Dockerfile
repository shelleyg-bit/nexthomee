FROM python:3.8

COPY ./src /root/nexthomee
COPY ./airflow_home /root/nexthomee/airflow_home

WORKDIR /root/nexthomee

RUN pip install "apache-airflow[celery]==2.2.4" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.8.txt"

CMD ["bash"]
