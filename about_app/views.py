from django.shortcuts import render
from django.views import View
from about_app.models import Objectives

class AboutView(View):
    def get(self, request):
        objectives_instances = Objectives.objects.filter().exclude(title='Objectives')
        main_instance = Objectives.objects.filter(title='Objectives')
        dictionary = {
            'objective_instances': objectives_instances,
            'main_instance': main_instance
        }

        return render(request, 'about.html', dictionary)
