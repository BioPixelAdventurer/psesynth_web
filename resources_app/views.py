from django.shortcuts import render
from django.views import View
from .models import PaperTemp

class ResourcesView(View):
    def get(self, request):
        instances = PaperTemp.objects.all()
        dictionary = {
            'instances': instances,
        }

        return render(request, 'resources.html', dictionary)