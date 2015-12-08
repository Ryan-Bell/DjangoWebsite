from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from .models import Patient, UserInfo, ProfileInfo, MedicalInfo
from .forms import BaseUserForm, UserForm, ProfileForm, MedicalForm
from django.views.decorators.csrf import csrf_exempt

"""
The views are essentially the intermediary step between the logic of the models and
database and the front facing html pages. These are what is being called in the urls.py
page. The format of each is fairly simple: At a minimum, the method needs to take a request,
however, as seen in the methods dealing with the patient, optional additional parameters can
be passed in through the urls.py page.
There are two types of request; GET and POST. Get is when the user is pulling the page and
Post is when they have entered some information and are submitting it to our side. When
dealing with a page that requires the user to input information, the general flow is to first
check what method the request is, displaying the blank forms if it is get, or pulling in the data
and using it somehow.

These @csrf_exempt lines above each view is a workaround solution for csrf missing token
errors. The error has something to do with a csrf tag not being placed properly in the
html files.
"""

@csrf_exempt
def userLogin(request):
    auth = 3
    if request.method == 'POST':
        #This is how data can be pulled from a post request. The 'username' and 'password' are assigned names for
        #the fields in the html page.
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate returns true or false based on whether the username and password match in the database
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                auth = 0
                return HttpResponseRedirect('/%s/profile' % username)
            else:
                auth = 1
                #all users have a is_valid field that can be toggled for expiration or transfers etc.
                return render(request, 'login.html', {'authenticated': auth , 'username' : username, 'password' : password})
        else:
            auth = 2
            return render(request, 'login.html', {'authenticated': auth , 'username' : username, 'password' : password})
    else:
        return render(request, "login.html", {'authenticated':auth})

@csrf_exempt
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

#TODO adjust the entire register method so that it works with the new html page
@csrf_exempt
def register(request):
    registered = False
    print("\nregister view entered")
    if request.method == 'POST':
        print("\nregister entered with POST")
        #this is where all of the data the user input is gathered.
        baseUserForm = BaseUserForm(data=request.POST)
        print("\nregister POST baseUserFormCreated")
        userForm = UserForm(data=request.POST)
        print("\nregister POST userFormCreated")
        profileForm = ProfileForm(data=request.POST)
        print("\nregister POST profileFormCreated")
        medicalForm = MedicalForm(data=request.POST)
        print("\nregister POST medicalFormCreated")

        print("\nregister POST outside is_valid if")
        #The forms are checked to determine if they are valid. This is where required fields are checked.
        if  userForm.is_valid() and profileForm.is_valid() and medicalForm.is_valid():

            print("\nregister POST inside is_valid if")

            #creating the user object
            user = baseUserForm.save()
            user.set_password(user.password)

            #all adjusted values must be followed by a save call.
            user.save()
            print("\nregister POST user object created")

            patientUserInfo = userForm.save()
            patientProfileInfo = profileForm.save()
            patientMedicalInfo = medicalForm.save()
            print("\nregister POST 3 info objects created")

            patient = Patient(user=user, userInfo = patientUserInfo, profileInfo=patientProfileInfo, medicalInfo=patientMedicalInfo)
            print("\nregister POST patient created")

            patient.user.save()
            patient.userInfo.save()
            patient.profileInfo.save()
            patient.medicalInfo.save()

            patient.save()
            print("\nregister POST patient info objects assigned")

            patient.user.first_name = patient.profileInfo.firstName
            patient.user.last_name = patient.profileInfo.lastName
            patient.user.email = patient.profileInfo.email
            patient.user.save()
            print("\nregister POST user first/last name updated")

            registered = True

            print("\nregister POST about to call profile")
            userLogin(request)
            print("\nThe following will not be reached but needs to be there to prevent errors:wq")
            return HttpResponseRedirect('/%s/profile' % patient.user.username)
        else:
            #these errors should be added into the registration.html so the user can see it
            print(baseUserForm.errors, userForm.errors, profileForm.errors, medicalForm.errors)
    else:
        print("\nregister GET creating blank forms")
        #if the request is get, show blank forms.
        baseUserForm = BaseUserForm()
        userForm = UserForm()
        profileForm = ProfileForm()
        medicalForm = MedicalForm()
        print("\nregister GET blank forms created")
    return render(request, 'registration.html', {'baseUserForm':baseUserForm, 'userForm':userForm, 'profileForm':profileForm, 'medicalForm':medicalForm, 'registered': registered})

@csrf_exempt
def profile(request, username):
    #check that the user is actually logged in so they can't access someone's profile just
    #by knowing the url. If they aren't authenticated they get redirected to the login page
    #using the reverse lookup which searches the urls in urls.py for a name of 'login'
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        #capture the user object and run checks on the account type to determine where to send them
        #In the future we may need to check for doctors and nurses and send them elsewhere.
        activeUser = Patient.objects.get(user=request.user)
    return render(request, 'ProfilePage.html', {'user' : activeUser})