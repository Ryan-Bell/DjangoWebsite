from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .forms import LoginForm

def loginPage(request):
#    name = "Ryan"
#    t = get_template('loginPage.html')
#    html = t.render(Context({'username':name}))
#    return HttpResponse(html)
    if request.method == 'POST':
        print("Enter post")
        form = LoginForm(request.POST)
        if form.is_valid():
            #need to check if user is in the database here
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('/tempProfilePage')
    else:
        form = LoginForm()

    return render(request, 'loginPage.html', {'LoginForm': form})


#def createPatient(request):
