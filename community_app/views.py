from django.shortcuts import render
from django.views import View
from .models import Participant

class ParticipantView(View):
    def get(self, request):
        instances = Participant.objects.filter()
        dictionary = {
            'instances': instances,
        }
        return render(request, 'community.html', dictionary)
