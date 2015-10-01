from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .forms import LoginForm, PatientRegisterForm, PatientProfileForm
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from django.contrib.auth.models import User, Group

@csrf_exempt  #workaround temp
def loginPage(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                #user = Group.objects.get_by_natural_key(form.cleaned_data['username'])
                #user = Patient._check_id_field(form.username)#User.objects.get(username=form.cleaned_data['username'])
                #all_Patients =
                return HttpResponse(Patient.check_password(form.cleaned_data['password']))
                #if(user.check_password(form.cleaned_data['password']) == False):
                if(Patient.check_password(form.cleaned_data['password']) == False):
                    return HttpResponse("Invalid Password")
            except: #User.DoesNotExist:
                user = None
            if(user != None):
                return HttpResponseRedirect('/patientProfile/' + form.cleaned_data['username'])
            else:
                return HttpResponse("User shown as not existing")
    else:
        form = LoginForm()
    return render(request, 'loginPage.html', {'LoginForm': form})

@csrf_exempt #workaround temp
def patientRegister(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            patient = Patient()
            #return HttpResponse(form.cleaned_data['username'])
            data = form.cleaned_data
            #return HttpResponse(data['password'])
            patient.password = data['password']
            patient.identifier = data['username']
            patient.address = data['address']
            patient.contactICEName = data['contactICEName']
            patient.contactICEPhone = data['contactICEPhone']
            patient.contactICERelationship = data['contactICERelationship']
            patient.country = data['country']
            #patient.dateBirth = form.
            patient.email = data['email']
            patient.firstName = data['firstName']
            patient.middleName = data['middleName']
            patient.lastName = data['lastName']
            patient.phonePrimary = data['phonePrimary']
            patient.phoneSecondary = data['phoneSecondary']
            patient.save()
            #user = Patient.
            #user = User.objects._create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'], False, False)
            #user.save()

            return HttpResponse("New Patient Created")
    else:
        form = PatientRegisterForm()

    return render(request, 'patientRegistration.html', {'PatientRegisterForm': form})

@csrf_exempt
def patientProfile(request, username):
    #return HttpResponse(username)
    form = PatientProfileForm(request.GET, nameArg='username')
    return render(request, 'patientProfile.html', {'PatientProfileForm': form})

