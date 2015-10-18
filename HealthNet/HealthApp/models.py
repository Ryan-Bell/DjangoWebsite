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
    dateOfBirth = models.DateField(blank=True)
    address = models.CharField(max_length=MAX_LENGTH, blank=True)
	
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
	   
class LogItem(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=MAX_LENGTH)
