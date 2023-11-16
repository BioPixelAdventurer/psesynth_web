import subprocess
from pathlib import Path
import shutil
import os

# Always run on /Users/ptest/temporal

# Define your pages
pages_to_bake = [
    {
        'output': 'tostatic/baked/index.html',
        'django_app': 'psesyn_app',
        'view': 'HomeView',
        'model': 'Home'
    },
    {
        'output': 'tostatic/baked/about.html',
        'django_app': 'about_app',
        'view': 'AboutView',
        'model': 'Objectives'
    },
    {
        'output': 'tostatic/baked/community.html',
        'django_app': 'community_app',
        'view': 'ParticipantView',
        'model': 'Participant'
    },
    {
        'output': 'tostatic/baked/news.html',
        'django_app': 'news_app',
        'view': 'NewsView',
        'model': 'News'
    },
    {
        'output': 'tostatic/baked/resources.html',
        'django_app': 'resources_app',
        'view': 'ResourcesView',
        'model': 'PaperTemp'
    },
    {
        'output': 'tostatic/baked/join.html',
        'django_app': 'join_app',
        'view': 'static_page',
    }
    # Add more pages as needed
]

# Path to your existing script
script_path = 'tostatic/baking_home.py'

# Iterate over pages and call the script for each
for page in pages_to_bake:
    # Start with the basic command
    command = [
        'python', script_path,
        '--output', page['output'],
        '--django_app', page['django_app'],
        '--view', page['view'],
    ]

    # Add the model argument if it exists
    if 'model' in page:
        command.extend(['--model', page['model']])

    # Run the subprocess with the constructed command
    subprocess.run(command)

htmls = Path('tostatic/baked').glob('*.html')

for html in htmls:
    if html.name == 'index.html':
        continue

    new_dir = html.parent / html.stem

    if new_dir.exists():
        shutil.rmtree(str(new_dir))

    new_dir.mkdir(exist_ok=True, parents=True)
    shutil.move(str(html), f'{new_dir}/index.html')




