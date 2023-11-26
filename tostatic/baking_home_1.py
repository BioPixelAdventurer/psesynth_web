import os
import django
import argparse
import importlib
from django.http import HttpRequest, QueryDict
import sys
sys.path.append('/Users/Lsine/ptest/temporal')

# Create the parser
parser = argparse.ArgumentParser(description='Convert Django view to static HTML for specific pages')

# Add arguments
parser.add_argument('--output', type=str, required=True, help='Output HTML file name')
parser.add_argument('--django_app', type=str, required=True)
parser.add_argument('--view', type=str, required=True)
parser.add_argument('--model', type=str, required=False, help='Django model name')  # Add this line

# Parse the arguments
args = parser.parse_args()

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psesyn.settings")
django.setup()

# Import the views module
views_module = importlib.import_module(f"{args.django_app}.views")

# Function to generate static page
def generate_static_page(output_filename, query_params):
    request = HttpRequest()
    request.method = 'GET'
    request.GET = query_params

    view = getattr(views_module, args.view)

    if hasattr(view, 'as_view'):
        response = view.as_view()(request)
    else:
        response = view(request)

    if hasattr(response, 'render') and callable(response.render):
        response.render()

    html_content = response.content.decode()

    with open(output_filename, 'w') as file:
        file.write(html_content)

# Check if the view is for the community section
if args.view == 'ParticipantView':  
    # Generate page for Coordinators
    generate_static_page(args.output + '_coordinators.html', QueryDict('roll=Coordinator'))

    # Generate page for Participants
    generate_static_page(args.output + '_participants.html', QueryDict('roll=Participant'))
