from django.contrib import admin
from .models import Patient, UserInfo, ProfileInfo, MedicalInfo

#This is how to control what models are visible to the admin.
admin.site.register(Patient)
admin.site.register(UserInfo)
admin.site.register(ProfileInfo)
admin.site.register(MedicalInfo)