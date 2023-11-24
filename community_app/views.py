from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Participant

class ParticipantView(ListView):
    model = Participant
    context_object_name = 'instances'
    template_name = 'community.html'

    def get_queryset(self):
        roll_in = self.request.GET.get('roll', '')
        if roll_in:
            queryset = Participant.objects.filter(roll_s__roll=roll_in)
        else:
            queryset = Participant.objects.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roll_in = self.request.GET.get('roll', '')
        context['header_text'] = f'{roll_in}s' if roll_in else 'Participants'
        return context
