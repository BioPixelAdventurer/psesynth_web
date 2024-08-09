from django.shortcuts import render
from django.views import View
from .models import News

class NewsView(View):
    def get(self, request):
        # Fetch all news instances and order them by date (newest first)
        instances = News.objects.all().order_by('-date')
        insta_dict = {'instances': instances}

        return render(request, 'news.html', insta_dict)
