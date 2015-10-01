from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .forms import LoginForm, PatientRegisterForm
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from django.contrib.auth.models import User

@csrf_exempt  #workaround temp
def loginPage(request):
#    name = "Ryan"
#    t = get_template('loginPage.html')
#    html = t.render(Context({'username':name}))
#    return HttpResponse(html)
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            #need to check if user is in the database here
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
            except User.DoesNotExist:
                user = None
            if(user != None):
                return HttpResponseRedirect('/patientProfile/' + form.cleaned_data['username'])
            else:
                return HttpResponseRedirect('/invalidUsername')
    else:
        form = LoginForm()
        #return HttpResponseRedirect('./tempProfilePage2')

    return render(request, 'loginPage.html', {'LoginForm': form})

@csrf_exempt #workaround temp
def patientRegister(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data['firstName']
            #username = Patient()
            #username.firstName = form.cleaned_data['firstName']
            #username.middleName = form.cleaned_data['middleName']
            #username.lastName = form.cleaned_data['lastName']
            user = User.objects._create_user(form.cleaned_data['firstName'], form.cleaned_data['email'], form.cleaned_data['password'], False, False)
            #user.is_staff = False
            #user.is_superuser = False
            user.save()
            #return HttpResponse(User.objects.get(firstName__exact=="Ryan").email)
            return HttpResponseRedirect('/NewPatientCreated')
            #enter info into new patient object and insert into database
    else:
        form = PatientRegisterForm()

    return render(request, 'patientRegistration.html', {'PatientRegisterForm': form})

#@csrf_exempt
#def patientProfile(request, username):
    #make sure the username is valid
    #return HttpResponse("You have reached the profile page of " + username)
