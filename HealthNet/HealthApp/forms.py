from django import forms
from django.contrib.auth.forms import User
from .models import Patient, LogItem


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

class LogItemForm(forms.ModelForm):
    class Meta:
        model = LogItem
        fields = ('username',)
	
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'firstName',
            'middleName',
            'lastName',
            'email',
            'phoneNumber',
			'dateOfBirth',
            'address',
        )
