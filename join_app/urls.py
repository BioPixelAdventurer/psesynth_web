from django.urls import path
from .views import static_page

urlpatterns = [
    path('', static_page, name='join')
]