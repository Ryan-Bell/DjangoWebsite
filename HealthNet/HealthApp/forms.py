from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

class PatientRegisterForm(forms.Form):
    MAX_LENGTH = 50

    #Basic Info
    firstName = forms.CharField(label="First Name", max_length=MAX_LENGTH)
    middleName = forms.CharField(label="Middle Name", max_length=MAX_LENGTH)
    lastName = forms.CharField(label="Last Name", max_length=MAX_LENGTH)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
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

#class PatientProfileForm(forms.Form):

