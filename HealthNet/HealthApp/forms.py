from django import forms
from django.contrib.auth.forms import User
from .models import Profile, PatientProfile, LogItem


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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'firstName',
            'middleName',
            'lastName',
            'email',
            'phoneNumber',
			'dateOfBirth',
            'address',
        )

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = (
            'dateOfBirth',
            'address',
        )
