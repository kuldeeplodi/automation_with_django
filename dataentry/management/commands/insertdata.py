from django.core.management.base import  BaseCommand
from dataentry.models import Student



class Command(BaseCommand):
    help="insert data "

    def handle(self,*args,**kwargs):
        # logic code
        dataset=[
            {"roll_no":2001,"name":"kuldeep","age":23},
            {"roll_no":2002,"name":"rohit","age":24},
            {"roll_no":2003,"name":"kunal","age":22},

        ]

        for data in dataset:
            exist=Student.objects.filter(roll_no=data["roll_no"]).exists()
            if not exist:
                  Student.objects.create(roll_no=data["roll_no"],name=data["name"],age=data["age"])
            else:
                   self.stdout.write(self.style.WARNING(f"roll no {data['roll_no']} of this student already exist"))
        self.stdout.write(self.style.SUCCESS("data is inserted successfully!"))


