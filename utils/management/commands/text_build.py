# in a file named batch_import.py inside a management/commands directory in one of your apps
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Batch import text from multiple files to multiple models based on a list in a text file.'

    def add_arguments(self, parser):
        parser.add_argument('list_file_path', type=str, help='The path to the text file containing the list of app names, model names, and file paths.')

    def handle(self, *args, **kwargs):
        list_file_path = kwargs['list_file_path']

        with open(list_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            app_name, model_name, file_path = line.strip().split()  # Assumes space-separated values
            call_command('import_text', file_path, app_name, model_name)
