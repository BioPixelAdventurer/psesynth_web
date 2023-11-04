from django.core.management.base import BaseCommand
from django.apps import apps
import datetime

class Command(BaseCommand):
    help = '''
    Import text from a file and save to a specified model.
    
    Usage:
    ------
    bash:
    path='path/to/your/file.txt'
    python manage.py home_build $path app_name model_name
    python manage.py home_build path/to/your/other_file.txt myotherapp OtherItem
    '''

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the text file to import')
        parser.add_argument('app_name', type=str, help='The name of the app containing the model')
        parser.add_argument('model_name', type=str, help='The name of the model to save the text to')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        app_name = kwargs['app_name']
        model_name = kwargs['model_name']

        with open(file_path, 'r') as file:
            text = file.read()

        html_content = self.text_to_html(text)

        # Get the model class
        ModelClass = apps.get_model(app_name, model_name)

        # Create a new record
        ModelClass.objects.create(
            title='Home',  # Adjust this as necessary
            content=html_content,
        )

    def text_to_html(self, text):
        paragraphs = text.split('\n\n')  # Assuming a blank line between paragraphs
        html_paragraphs = [f'<p>{p}</p>' for p in paragraphs]
        return '\n'.join(html_paragraphs)
    