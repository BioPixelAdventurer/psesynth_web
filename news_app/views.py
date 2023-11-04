from django.shortcuts import render
from django.views import View
from .models import News

class NewsView(View):
    def get(self, request):

        instances = News.objects.all()
        insta_dict = {'instances': instances}

        return render(request, 'news.html', insta_dict)
