from awd_main.celery import app
import time
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
from .util import send_email_notification


@app.task
def celery_task_test():
    time.sleep(10)
    mail_subject="celery task executed"
    message="this is a test email sent from celery task"
    to_email=settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
  
    return "email send successfully"


@app.task
def import_data_task(file_path,model_name):
    try:
      call_command('importdata',file_path,model_name)
                
    except Exception as e:
                 raise e
    mail_subject="import data completed"
    message="your data is imported successfully from csv file to database"
    to_email=settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return "data imported successfully and email send successfully"
    


