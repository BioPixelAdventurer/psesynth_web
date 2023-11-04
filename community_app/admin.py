from django.contrib import admin
from .models import Participant, Country,Tag, StudyField, Institution, Roll

admin.site.register(Participant)
admin.site.register(Country)
admin.site.register(Tag)
admin.site.register(StudyField)
admin.site.register(Institution)
admin.site.register(Roll)
