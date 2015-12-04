from django.contrib import admin
from .models import Patient
#This is how to control what models are visible to the admin.
#They are first imported then registered. Yes, it's that easy.
admin.site.register(Patient)