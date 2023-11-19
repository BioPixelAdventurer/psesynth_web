from django.contrib import admin
from .models import PaperTemp, PubType, Author, Year, Authorship, Group

admin.site.register(PaperTemp)
admin.site.register(PubType)
admin.site.register(Author)
admin.site.register(Year)
admin.site.register(Authorship)
admin.site.register(Group)
# Register your models here.
