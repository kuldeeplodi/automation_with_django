from awd_main.celery import app
import time
from django.core.management import call_command


@app.task
def celery_task_test():
    time.sleep(10)
    return "task executed successfully"


def import_data_task(file_path,model_name):
    try:
      call_command('importdata',file_path,model_name)
                
    except Exception as e:
                 raise e