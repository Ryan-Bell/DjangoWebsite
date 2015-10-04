from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .models import Patient
from django.contrib.auth.models import User, Group

def loginPage(request):
    return

def patientRegister(request):
    if request.method == 'POST':
        patient = Patient()

        patient.identifier = request.POST["identifier"]
        patient.firstName = request.POST["firstName"]
        patient.middleName = request.POST["middleName"]
        patient.lastName = request.POST["lastName"]
        patient.addressNumber = request.POST["addressNumber"]
        patient.addressStreet = request.POST["addressStreet"]
        patient.addressCity = request.POST["addressCity"]
        patient.addressState = request.POST["addressState"]
        patient.addressZip = request.POST["addressZip"]
        patient.phone = request.POST["phone"]
        patient.dob = request.POST["dob"]
        patient.sex = request.POST["sex"]
        patient.contactName = request.POST["contactName"]
        patient.contactRelationship = request.POST["contactRelationship"]
        patient.contactPhone = request.POST["contactPhone"]

        patient.tuberculosis = request.POST["tuberculosis"]
        patient.influenza = request.POST["influenza"]
        patient.rheumatic = request.POST["rheumatic"]
        patient.whoopingCough = request.POST["whoopingCough"]
        patient.tonsillitis = request.POST["tonsillitis"]
        patient.measles = request.POST["measles"]
        patient.mumps = request.POST["mumps"]
        patient.frequentColds = request.POST["frequentColds"]
        patient.germanMeasles = request.POST["germanMeasles"]
        patient.scarletFever = request.POST["scarletFever"]
        patient.scarlatina = request.POST["scarlatina"]
        patient.diphtheria = request.POST["diphtheria"]
        patient.polio = request.POST["polio"]
        patient.chickenpox = request.POST["chickenpox"]
        patient.coxsackie = request.POST["coxsackie"]
        patient.pneumonia = request.POST["pneumonia"]
        patient.diabetes = request.POST["diabetes"]
        patient.dtype = request.POST["dtype"]
        patient.cancer = request.POST["cancer"]
        patient.ctype = request.POST["ctype"]


        patient.highBloodPressure = request.POST["highBloodPressure"]
        patient.migraine = request.POST["migraine"]
        patient.strokes = request.POST["strokes"]
        patient.kidneyDisease = request.POST["kidneyDisease"]
        patient.arthritis = request.POST["arthritis"]
        patient.allergy = request.POST["allergy"]
        patient.bleeding = request.POST["bleeding"]
        patient.syphilis = request.POST["syphilis"]
        patient.anemia = request.POST["anemia"]
        patient.obesity = request.POST["obesity"]
        patient.epilepsy = request.POST["epilepsy"]

        patient.save()
        return HttpResponse("A new user has been registered! ...maybe")
    return render(request, '../html/patientRegistration.html')

#def patientProfile(request, username):
    #return HttpResponse(username)
 #   form = PatientProfileForm(request.GET, nameArg='username')
  #  return render(request, 'patientProfile.html', {'PatientProfileForm': form})

