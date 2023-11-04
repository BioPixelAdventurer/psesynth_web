from django.shortcuts import render
from django.views import View
from .models import Home

class HomeView(View):
    def get(self, request):
        home_instances = Home.objects.all()
        return render(request, 'index.html', {'home_instances': home_instances})

