from django.core.management.base import  BaseCommand,CommandError
from dataentry.models import Student
import csv
from django.apps import apps


class Command(BaseCommand):
    help="import data from csv file"

    def add_arguments(self, parser):
        parser.add_argument("file_path",type=str,help="path to the csv file")
        parser.add_argument("model_name",type=str,help="")

    def handle(self,*args,**kwargs):
        # logic code
        file_path=kwargs["file_path"]
        model_name=kwargs["model_name"].capitalize()


        # search for the model
        model=None
        for app_config in apps.get_app_configs():
         try:
            model=apps.get_model(app_config.label,model_name)
            break
         except LookupError:
            continue

        if not model:
            raise CommandError(f"Model {model_name} does not found! ")
        
        with open(file_path,"r") as file:
            records=csv.DictReader(file)
            for data in records:
               model.objects.create(**data)
       
        self.stdout.write(self.style.SUCCESS("data are import from csv  successfully!"))


