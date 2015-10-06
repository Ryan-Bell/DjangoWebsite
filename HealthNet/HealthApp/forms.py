from django import forms
from django.contrib.auth.forms import User
from .models import Profile, PatientProfile


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

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
        )

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = (
            'dateOfBirth',
            'address',
        )

"""
class PatientRegisterForm(forms.Form):
    MAX_LENGTH = 50
    username = forms.CharField(label="Username", max_length=MAX_LENGTH)
    firstName = forms.CharField(label="First Name", max_length=MAX_LENGTH)
    middleName = forms.CharField(label="Middle Name", max_length=MAX_LENGTH)
    lastName = forms.CharField(label="Last Name", max_length=MAX_LENGTH)

    #MALE = 'M'
    #FEMALE = 'F'
    #GENDER_CHOICES = (
    #    (MALE, 'Male'),
    #    (FEMALE, 'Female'),
    #)
    #gender = forms.CharField(label="Gender", max_length=2, choices=GENDER_CHOICES, default=MALE)
    #dateBirth = forms.DateField(label="Date of Birth", verbose_name="Date of Birth")
    phonePrimary = forms.CharField(label="Primary Phone", max_length=MAX_LENGTH)
    phoneSecondary = forms.CharField(label="Secondary Phone", max_length=MAX_LENGTH)
    email = forms.EmailField(label="Email Address", max_length=MAX_LENGTH)
    country = forms.CharField(label="Country of Birth", max_length=MAX_LENGTH)
    address = forms.CharField(label="Full Address", max_length=MAX_LENGTH)
    contactICEName = forms.CharField(label="Emergency Contact Name", max_length=MAX_LENGTH)
    contactICERelationship = forms.CharField(label="Emergency Contact Relationship", max_length=MAX_LENGTH)
    contactICEPhone = forms.CharField(label="Emergency Contact Phone", max_length=MAX_LENGTH)
    provider = forms.CharField(label="Insurance Provider", max_length=MAX_LENGTH)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=MAX_LENGTH)

class PatientProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        nameArg = kwargs.pop('nameArg')
        #self.fields['nameArg'].initial = nameArg
        super(PatientProfileForm, self).__init__(*args, **kwargs)
    MAX_LENGTH = 50
    try:
        user = User.objects.get(username='nameArg')
    except:
        user = None
    if (user != None):
        fname = forms.CharField(max_length=MAX_LENGTH, default=user.firstName, editable=False)
    #else:
     #   fname = forms.CharField(max_length=MAX_LENGTH, default=user.firstName, editable=False)
"""""