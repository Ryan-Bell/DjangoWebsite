from django import forms
from django.contrib.auth.forms import User
from .models import Patient, LogItem, MedicalInfo, InsuranceInfo, Profile


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
            'middleInitial',
            'lastName',
            'socialSecurity',
            'citizen',
            'sex',
            'email',
            'phoneNumber',
			'dateOfBirth',
            'address',
            'city',
            'state',
            'zipcode',
        )

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = InsuranceInfo
        fields = (
            'provider',
            'policyNumber',
            'groupNumber',
            'policyExpirationDate',
            'premiumAmount',
            'policyType',
        )

class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalInfo
        fields = (
            'tuberculosis',
            'influenza',
            'rheumatic',
            'whoopingCough',
            'tonsillitis',
            'measles',
            'mumps',
            'frequentColds',
            'germanMeasles',
            'scarletFever',
            'scarlatina',
            'diphtheria',
            'polio',
            'chickenpox',
            'coxsackie',
            'pneumonia',
            'highBloodPressure',
            'migraine',
            'strokes',
            'kidneyDisease',
            'arthritis',
            'allergy',
            'bleeding',
            'syphilis',
            'anemia',
            'obesity',
            'epilepsy',
        )

