from django.urls import path
from .views import ParticipantView, CoordView

urlpatterns = [
    path('coordinators', CoordView.as_view(), name='coord'),
    path('participants', ParticipantView.as_view(), name='parti'),
]