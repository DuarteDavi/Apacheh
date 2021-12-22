from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.bash_operator import BashOperator


default_args = {
   'owner': 'pablo_brenner',
   'depends_on_past': False,
   'start_date': datetime(2019, 1, 1),
   'retries': 0,
   }


   
   
with DAG(
   'my-first-dag',
   schedule_interval=timedelta(minutes=1),
   catchup=False,
   default_args=default_args
   ) as dag:

    t1 = BashOperator(
    task_id='first_etl',
    bash_command="""
    cd $AIRFLOW_HOME/dags/etl_scripts/
    python3 my_first_etl_script.py
    """)
    t2 = BashOperator(
   task_id='second_etl',
   bash_command="""
   cd $AIRFLOW_HOME/dags/etl_scripts/
   python3 my_second_etl_script.py
   """)
t1 >> t2