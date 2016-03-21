from django.contrib import admin
from .models import Patient, UserInfo, ProfileInfo, MedicalInfo, Doctor, Nurse, Hospital, Prescription, MedTest

#This is how to control what models are visible to the admin.
admin.site.register(Patient)
admin.site.register(UserInfo)
admin.site.register(ProfileInfo)
admin.site.register(MedicalInfo)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Hospital)
admin.site.register(Prescription)
admin.site.register(MedTest)