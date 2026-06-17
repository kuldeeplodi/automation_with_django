from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="greets the user"

    def add_arguments(self, parser):
          parser.add_argument('name',type=str,help="specifies user name")

    def handle(self,*args,**kwargs):
        #  write the logic
        name=kwargs['name']
        greeting=f"HI {name}, good morning!"
        self.stdout.write(greeting)