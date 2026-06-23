from django.core.management.base import  BaseCommand,CommandError
from dataentry.models import Student
import csv
from django.apps import apps
from django.db import DataError
from dataentry.util import check_csv_error


class Command(BaseCommand):
    help="import data from csv file"

    def add_arguments(self, parser):
        parser.add_argument("file_path",type=str,help="path to the csv file")
        parser.add_argument("model_name",type=str,help="")

    def handle(self,*args,**kwargs):
        # logic code
        file_path=kwargs["file_path"]
        model_name=kwargs["model_name"].capitalize()

        model=check_csv_error(file_path,model_name)

        with open(file_path,"r") as file:
            records=csv.DictReader(file) 
            for data in records:
                  model.objects.create(**data)
       
        self.stdout.write(self.style.SUCCESS("data are import from csv  successfully!"))


