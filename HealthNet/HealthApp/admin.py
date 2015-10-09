from django.contrib import admin
from .models import Profile, PatientProfile, LogItem
# Register your models here.

admin.site.register(Profile)
admin.site.register(PatientProfile)
admin.site.register(LogItem)