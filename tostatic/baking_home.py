import os
import django
import argparse
import importlib
from django.template.loader import render_to_string
from django.http import HttpRequest
import sys
sys.path.append('/Users/Lsine/ptest/temporal')

# Create the parser
parser = argparse.ArgumentParser(description='Convert Django view to static HTML')

# Add arguments
parser.add_argument('--output', type=str, required=True, help='Output HTML file name')
parser.add_argument('--django_app', type=str, required=True)
parser.add_argument('--view', type=str, required=True)
parser.add_argument('--model', type=str, required=False)

# Parse the arguments
args = parser.parse_args()

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psesyn.settings")
django.setup()

# Dynamic imports
if args.model:

    models_module = importlib.import_module(f"{args.django_app}.models")
    ModelClass = getattr(models_module, args.model)
views_module = importlib.import_module(f"{args.django_app}.views")

# Fetch the model and view class using getattr
ViewClass = getattr(views_module, args.view)

# Simulate a request and call the view
request = HttpRequest()
request.method = 'GET'

view = getattr(views_module, args.view)

# Call the view based on its type
if hasattr(view, 'as_view'):
    # It's a class-based view
    response = view.as_view()(request)
else:
    # It's a function-based view
    response = view(request)

html_content = response.content.decode('utf-8')

# Write the rendered content to the specified HTML file
with open(args.output, 'w', encoding='utf-8') as file:
    file.write(html_content)
