from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from abc import ABCMeta, abstractclassmethod

TYPES = (
    ('Patient', 'Patient'),
    ('Doctor', 'Nurse'),
    ('Nurse', 'Nurse'),
    ('Admin', 'Admin')
)

MAX_LENGTH = 50

class Profile(models.Model):
    user = models.OneToOneField(User)
    #type = models.CharField(max_length=10, types=TYPES)
    type = models.CharField(max_length=10)
    firstName = models.CharField(max_length=MAX_LENGTH)
    middleName = models.CharField(max_length=MAX_LENGTH, blank=True)
    lastName = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(blank=False)
    phoneNumber = models.CharField(max_length=14)

    def __str__(self):
        return self.user.username

    def getName(self):
        return self.firstName + " " + self.lastName

    def getType(self):
        return self.type

class PatientProfile(models.Model):
   profile = models.OneToOneField(Profile)
   dateOfBirth = models.DateField()
   address = models.CharField(max_length=MAX_LENGTH)

   def __str__(self):
       return self.profile.user.username

   def getName(self):
       return self.profile.firstName + " " + self.profile.lastName

"""
class Patient(AbstractBaseUser):
    user = models.OneToOneField(User)
    MAX_LENGTH = 50
    identifier = models.CharField(max_length=MAX_LENGTH, unique=True)
    USERNAME_FIELD = 'identifier'

    firstName = models.CharField(max_length=MAX_LENGTH)
    middleName = models.CharField(max_length=MAX_LENGTH)
    lastName = models.CharField(max_length=MAX_LENGTH)
    phonePrimary = models.CharField(max_length=MAX_LENGTH)
    phoneSecondary = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH)
    country = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)
    contactICEName = models.CharField(max
    length=MAX_LENGTH)
    contactICERelationship = models.CharField(max_length=MAX_LENGTH)
    contactICEPhone = models.CharField(max_length=MAX_LENGTH)
    provider = models.CharField(max_length=MAX_LENGTH)

    REQUIRED_FIELDS = [firstName,lastName,phonePrimary,email,country,address,provider]
"""