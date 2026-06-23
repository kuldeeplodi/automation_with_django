from django.core.mail import EmailMessage

from django.apps import apps
import csv

from awd_main import settings
from django.db import DataError
from django.core.management.base import CommandError


def get_custom_model_name():
    defualt_name=['LogEntry','Permission','Group','User','ContentType','Session']

    custom_model=[]
    for model in apps.get_models():
        if model.__name__ not in defualt_name:
             custom_model.append(model.__name__)
    return custom_model



def check_csv_error(file_path,model_name):
            # search for the model
        model=None
        for app_config in apps.get_app_configs():
         try:
            model=apps.get_model(app_config.label,model_name)
            break
         except LookupError:
            continue # model not found in this app,continue searching in next app
        
        if not model:
            raise CommandError(f"Model {model_name} does not found! ")
        
        model_field=[field.name for field in model._meta.fields if field.name != "id"]

        try:
            with open(file_path,"r") as file:
                records=csv.DictReader(file)
                csv_field=records.fieldnames
                 
                #  comapare csv header with model's field name
                if csv_field != model_field:
                  raise DataError(f'csv file does not match {model_name} table field')
        except Exception as e:
            raise e
        
        return model



def send_email_notification(mail_subject,message,to_email):
    try:
        from_email=settings.EMAIL_HOST_USER
        mail=EmailMessage(mail_subject,message,from_email,to=[to_email])
        mail.send()
    except Exception as e:
        raise e
   
  