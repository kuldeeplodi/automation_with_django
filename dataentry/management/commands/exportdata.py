from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv
import datetime
from django.apps import apps


class Command(BaseCommand):
    help="export data from database to csv file"

    def add_arguments(self, parser):
             parser.add_argument("model_name",type=str,help="path to the csv file")

    def handle(self,*args,**kwargs):

        model_name=kwargs["model_name"].capitalize()


        # search the model name
        model=None
        for app_config in apps.get_app_configs():
         try:
            model=apps.get_model(app_config.label,model_name)
            break

         except LookupError:
               pass
       
        if not model:
            self.stderr.write(f"model {model_name} could not found")
            return
        
        data=model.objects.all()
         
        timestamp=datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
      
        file_path=f"export_student_data_{timestamp}.csv"
        
        with open(file_path,"w",newline='') as file:

            write=csv.writer(file)
            

            # create csv header
            write.writerow([field.name for field in model._meta.fields])

            for dt in data:
             write.writerow([getattr(dt,field.name) for field in model._meta.fields])


        self.stdout.write(self.style.SUCCESS("export data from database successful!"))