from django.contrib import admin
from .models import PaperTemp, PubType, Author, Year

admin.site.register(PaperTemp)
admin.site.register(PubType)
admin.site.register(Author)
admin.site.register(Year)
# Register your models here.
