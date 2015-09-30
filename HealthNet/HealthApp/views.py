from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def loginPage(request):
    #return HttpResponse("You are on the login page")
    name = "Ryan"
    t = get_template('loginPage.html')
    html = t.render(Context({'username':name}))
    return HttpResponse(html)