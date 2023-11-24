from django.shortcuts import render
from django.views import View
from .models import Participant

class CoordView(View):
    def get(self, request):
        instances = Participant.objects.filter(roll_s__roll='Coordinator')
        dictionary = {
            'instances': instances,
            'header_text':'Coordinators'
        }
        return render(request, 'coordinators.html', dictionary)

class ParticipantView(View):
    def get(self, request):
        instances = Participant.objects.filter(roll_s__roll='Participant')
        dictionary = {
            'instances': instances,
            'header_text':'Participants'
        }
        return render(request, 'participants.html', dictionary)
