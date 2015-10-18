from django.contrib import admin
from .models import Patient, LogItem
#This is how to control what models are visible to the admin.
#They are first imported then registered. Yes, it's that easy.
admin.site.register(Patient)
admin.site.register(LogItem)