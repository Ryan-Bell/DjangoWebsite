from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from .models import Patient
from .forms import UserForm, PatientForm, LogItemForm
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
html files. I have tried multiple arrangements but ended up using this workaround in the
interest of time. These csrf(cross-site request forgery) tokens are used for security
purposes and will most likely not play a huge role in this class assignment.
"""
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
        activeUser = request.user
        name = activeUser.first_name
        #show the user a rendered html page patientProfile.html and pass in the user object and name.
        #The parameters are passed in to the html page with the name 'name' and 'user'.
        return render(request, 'patientProfile.html', {'name': name, 'user':activeUser})
@csrf_exempt
def profileAppointments(request, username):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        activeUser = request.user
        name = activeUser.first_name
        return render(request, 'patientAppointment.html', {'name': name, 'user':activeUser})
@csrf_exempt
def profileMedicalInfo(request, username):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        activeUser = request.user
        name = activeUser.first_name
        return render(request, 'patientMedicalInfo.html', {'name': name, 'user':activeUser})

@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        #this is where all of the data the user input is gathered. Forms are filled out with
        #the entered data.
        userForm = UserForm(data=request.POST)
        patientForm = PatientForm(data=request.POST)
        itemLogForm = LogItemForm(data=request.POST)
        #The forms are checked to determine if they are valid. This is where required fields are checked.
        #This is bulid into django and the else statement easily displays to the user the location of their folly.
        if userForm.is_valid()and patientForm.is_valid():
            #creating the user object
            user = userForm.save()

            user.set_password(user.password)
            #all adjusted values must be followed by a save call.
            user.save()
            #Create the log item object and save it
            item = itemLogForm.save(commit=False)
            item.user = user
            item.username = user.username
            item.save()
            #create and save the patient profile
            patientProfile = patientForm.save(commit=False)
            patientProfile.user = user
            patientProfile.save()
            user.first_name = patientProfile.firstName
            user.last_name = patientProfile.lastName
            user.save()
            registered = True
        else:
            print(userForm.errors, patientForm.errors)
    else:
        #if the request is get, show blank forms.
        userForm = UserForm()
        patientForm = PatientForm()
    return render(request, 'register.html', {'userForm':userForm, 'patientForm':patientForm, 'registered': registered})
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
                #all users have a is_valid field that can be toggled for expiration or transfers or whatever else we want in the future.
                return HttpResponse("Your healthnet account is innactive")
        else:
            auth = 2
            #currently, an invlaid login will display a blank page with only the text "Invlaid login"
            #the line below it would return them to the login page.
            return HttpResponse("Invalid Login")
            return render(request, 'login.html', {'authenticated': auth})
    else:
        return render(request, "login.html", {'authenticated':auth})
@csrf_exempt
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')
