"""HealthNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from HealthApp import views
from django.conf.urls.static import static
from django.conf import settings

"""
The urlpatterns is how we map the site urls to specific views in the views.py. The first part is
a regular expression to describe the url pattern, followed by the view that should be called.
Lastly, a name is given to each pattern so that they can be referenced from elsewhere in the code.
For example, when an HTTPResponseRedirect(reverse('login')) is returned in one of the views, it
is doing a reverse lookup of the url pattern named 'login' and returning the view (and subsequently
the html page) associated with the view.

There are a couple patterns that are a bit unique. The first is the url for the admin page which
links to the built in url network already created by django. The other unique urls are the ones
that deal with patient information since the urls are specific to the patient, and the username in
the url needs to be passed into the view as a parameter. The format of (?P<username>\w+) is used
to first identify that information is being captured, and to identify what parameter it is being passed
in as (in this case, the username parameter).

Note: the first url is used to redirect users to the login page when at the 'root' url of the site.
"""
urlpatterns = [
    url(r'^$', views.userLogin, name='login'),
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerMedical/$', views.registerMedical, name='registerMedical'),
    url(r'^logout/$', views.userLogout, name='logout'),
    #TODO change the admin link to not use django's built in admin site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<username>\w+)/profile/Appointments$', views.profileAppointments, name='calendar'),
    url(r'^(?P<username>\w+)/profile/MedicalInfo$', views.profileMedicalInfo, name='medical')
]