from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import User
<<<<<<< HEAD
from .models import Patient, UserInfo, MedicalInfo, ProfileInfo, Prescription, MedTest, LogItem, Appointment
=======
from .models import Patient, UserInfo, MedicalInfo, ProfileInfo, Prescription, MedTest, LogItem
>>>>>>> 734e0354649f156159a5548045f0613b85f55701


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

class BaseUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

<<<<<<< HEAD
class AppointmentForm(forms.Form):
		
		doctor = forms.CharField(max_length=50)
		date = forms.CharField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
		time = forms.CharField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
		description = forms.CharField(max_length=200)
		
		class Meta:
				model = Appointment
				fields = (
						'doctor',
						'userName',
						'date',
						'time',
						'description'
				)
		def __init__ (self, *args, **kwargs):
			super(AppointmentForm, self).__init__(*args, **kwargs)
			self.fields['date'].widget.attrs['value'] = '2015-03-14'
		
		
=======

>>>>>>> 734e0354649f156159a5548045f0613b85f55701
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
            'city',
            'state',
            'dateOfBirth',
            'zipcode',
            'phoneNumber',
            'email',
            'eName',
            'ePhoneNumber',
        )

class MedicalForm(ModelForm):
    class Meta:
        model = MedicalInfo
        fields = (
            #add cancer/diabetes
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

class MedTestForm(ModelForm):
    class Meta:
        model = MedTest
        fields = (
            'name',
            'doctor',
            'released',
            'dateIssued',
            'result',
        )

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = (
            'medicationCategory',
            'medication',
            'dosage',
            'frequency',
            'directions',
            'comments',
        )

class LogItemForm(ModelForm):
    class Meta:
        model = LogItem
        fields = (
            'user',
            'datetime',
            'action'
        )