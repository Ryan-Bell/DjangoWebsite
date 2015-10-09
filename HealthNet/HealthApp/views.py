from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from .models import Profile, PatientProfile
from .forms import UserForm, ProfileForm, PatientProfileForm, LogItemForm
#from .forms import LoginForm, PatientRegisterForm, PatientProfileForm
from django.views.decorators.csrf import csrf_exempt
#from .models import Patient
#from django.contrib.auth.models import User, Group

@csrf_exempt
def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        activeUser = request.user
        if activeUser.profile.type == 'Patient':
            name = activeUser.profile.getName()
        else:
            name = activeUser.username
        return render(request, 'HealthNet/html/home.html', {'name': name})
@csrf_exempt
def profile(request, username):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        activeUser = request.user
        if activeUser.profile.type == 'Patient':
            name = activeUser.profile.getName()
        else:
            name = activeUser.username
        return render(request, 'patientProfile.html', {'name': name, 'user':activeUser})
@csrf_exempt
def profileAppointments(request, username):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        activeUser = request.user
        if activeUser.profile.type == 'Patient':
            name = activeUser.profile.getName()
        else:
            name = activeUser.username
        return render(request, 'patientAppointment.html', {'name': name, 'user':activeUser})
		
@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        profileForm = ProfileForm(data=request.POST)
        patientProfileForm = PatientProfileForm(data=request.POST)
        itemLogForm = LogItemForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid() and patientProfileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            item = itemLogForm.save(commit=False)
            item.user = user
            item.username = user.username
            item.save()
            standardProfile = profileForm.save(commit=False)
            standardProfile.user = user
            standardProfile.type = 'Patient'
            standardProfile.save()
            patientProfile = patientProfileForm.save(commit=False)
            patientProfile.profile = standardProfile
            patientProfile.save()
            registered = True
        else:
            print(userForm.errors, profileForm.errors, patientProfileForm.errors)
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        patientProfileForm = PatientProfileForm()
    return render(request, 'register.html', {'userForm':userForm, 'profileForm': profileForm, 'patientProfileForm':patientProfileForm, 'registered': registered})
@csrf_exempt
def userLogin(request):
    auth = 3
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                auth = 0
                #return HttpResponseRedirect(reverse('home'))
                #return HttpResponse("You are logged in!")
                return HttpResponseRedirect('/%s/profile' % username)
            else:
                auth = 1
                return HttpResponse("Your healthnet account is innactive")
        else:
            #print("Invalid login: {0}, {1}".format(username, password))
            auth = 2
            return HttpResponse("Invalid Login")
            return render(request, 'login.html', {'authenticated': auth})
    else:
        return render(request, "login.html", {'authenticated':auth})
@csrf_exempt
def userLogout(request):
    #try:
        #if logout(request) != "":
    #        return HttpResponse("You have been logged out")
    #except:
    #    return HttpResponse("You have been logged out")
    #return HttpResponse("You have been logged out")
    #return HttpResponseRedirect('/')

    logout(request)
    return HttpResponseRedirect('/')















"""
#@csrf_exempt  #workaround temp
def loginPage(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                #user = Group.objects.get_by_natural_key(form.cleaned_data['username'])
                #user = Patient._check_id_field(form.username)#User.objects.get(username=form.cleaned_data['username'])
                #all_Patients =
                #return HttpResponse(Patient.check_password(form.cleaned_data['password']))
                #if(user.check_password(form.cleaned_data['password']) == False):
                data = form.cleaned_data
                #return HttpResponse(Patient.objects.all())
                #return HttpResponse(Patient.objects.filter(identifier=data['username']))
                user = Patient.objects.filter(identifier=data['username'])
                #return HttpResponse(user)
                #if(user.check_password(data['password']) == False):
                #    return HttpResponse("Invalid Password")
            except: #User.DoesNotExist:
                user = None
            if(user != None):
                return HttpResponseRedirect('/patientProfile/' + data['username'])
            else:
                return HttpResponse("User shown as not existing")
    else:
        form = LoginForm()
    return render(request, 'loginPage.html', {'LoginForm': form})

#@csrf_exempt #workaround temp
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

#@csrf_exempt
def patientProfile(request, username):
    #return HttpResponse(username)
    form = PatientProfileForm(request.GET, nameArg='username')
    return render(request, 'patientProfile.html', {'PatientProfileForm': form})

"""