from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from abc import ABCMeta, abstractclassmethod
"""
The models.py is essentially where objects are declared. Currently, It holds the
PatientProfile object and the logItem object. These objects are most always referenced
in the views. In each class, fields are declared by giving the name followed by the type
of input field. Many of the models have a OneToOne link to another model. ManyToOne,
OneToMany, and ManyToMany are also other types of multiplicities allowed. These link the models.
"""

#I don't exactly remember what this is for or why  past-Ryan created it and never
#used it. Nonetheless, I remember thinking it was a good idea at the time so I
#decided not to delete it for now.
TYPES = (
    ('Patient', 'Patient'),
    ('Doctor', 'Nurse'),
    ('Nurse', 'Nurse'),
    ('Admin', 'Admin')
)

#This is used to limit the entry boxes to 50 characters
MAX_LENGTH = 50

class Profile(models.Model):
    user = models.OneToOneField(User)
    #type = models.CharField(max_length=10, types=TYPES)
    type = models.CharField(max_length=10)
    firstName = models.CharField(max_length=MAX_LENGTH)
    #setting blank to true means this field will not be required
    middleName = models.CharField(max_length=MAX_LENGTH, blank=True)
    lastName = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(blank=False)
    phoneNumber = models.CharField(max_length=14)
    dateOfBirth = models.DateField(blank=True)
    address = models.CharField(max_length=MAX_LENGTH, blank=True)
	
    def __str__(self):
        return self.user.username
    #custom methods can be defined
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
