from django.urls import path
from .views import AboutView, SouthView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('south/', SouthView.as_view(), name='south')
]