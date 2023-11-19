from django.shortcuts import render
from django.views import View
from .models import PaperTemp

class ResourcesView(View):
    def get(self, request):
        objects = PaperTemp.objects.prefetch_related('authorship_set__author', 'year', 'publicationType', 'group').all()
        instances = []

        for obj in objects:
            authors_sort = obj.authorship_set.all().order_by('ranking')

            authors_info = [{'last_name': authorship.author.last_name, 
                'name_init': authorship.author.first_name[0]}
                for authorship in authors_sort]

            instances.append({
                'title':obj.title,
                'type': obj.publicationType.publicationType,
                'authors':authors_info,
                'group': obj.group.name,
                'year': obj.year.year,
                'thumbnail':obj.thumbnail.url,
                'link': obj.link
            })

        dictionary = {
            'instances': instances,
        }

        return render(request, 'resources.html', dictionary)