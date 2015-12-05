from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import User
from .models import Patient, UserInfo, MedicalInfo, ProfileInfo


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

"""
class LogItemForm(forms.ModelForm):
    class Meta:
        model = LogItem
        fields = ('username',)
"""

class BaseUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = (
            'policyNumber',
            'provider',
            'groupNumber',
        )


class ProfileForm(ModelForm):
    class Meta:
        model = ProfileInfo
        fields = (
            'firstName',
            'middleName',
            'lastName',
            'address',
            #'city',
            #'state',
            #'dateOfBirth',
            'zipcode',
            'phoneNumber',
            'email',
            #'contactName',
            #'contactPhoneNumber',
        )

class MedicalForm(ModelForm):
    class Meta:
        model = MedicalInfo
        fields = (
            'allergies',
            'anemia',
            'arthritis',
            'chickenpox',
            'coxsackie',
            'diphtheria',
            'epilepsy',
            'frequentColds',
            'germanMeasles',
            'highBloodPressure',
            'influenza',
            'kidneyDisease',
            'measles',
            'migraines',
            'mumps',
            'obesity',
            'pneumonia',
            'polio',
            'rheumaticFever',
            'scarlatina',
            'scarletFever',
            'strokes',
            'syphilis',
            'tonsillitis',
            'tuberculosis',
            'whoopingCough',
        )