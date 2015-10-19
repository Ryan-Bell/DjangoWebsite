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


class MedicalInfo(models.Model):
    tuberculosis = models.BooleanField(default=False)
    influenza = models.BooleanField(default=False)
    rheumatic = models.BooleanField(default=False)
    whoopingCough = models.BooleanField(default=False)
    tonsillitis = models.BooleanField(default=False)
    measles = models.BooleanField(default=False)
    mumps = models.BooleanField(default=False)
    frequentColds = models.BooleanField(default=False)
    germanMeasles = models.BooleanField(default=False)
    scarletFever = models.BooleanField(default=False)
    scarlatina = models.BooleanField(default=False)
    diphtheria = models.BooleanField(default=False)
    polio = models.BooleanField(default=False)
    chickenpox = models.BooleanField(default=False)
    coxsackie = models.BooleanField(default=False)
    pneumonia = models.BooleanField(default=False)
    highBloodPressure = models.BooleanField(default=False)
    migraine = models.BooleanField(default=False)
    strokes = models.BooleanField(default=False)
    kidneyDisease = models.BooleanField(default=False)
    arthritis = models.BooleanField(default=False)
    allergy = models.BooleanField(default=False)
    bleeding = models.BooleanField(default=False)
    syphilis = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User)
    medicalInfo = models.OneToOneField(MedicalInfo, null=True)
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

class LogItem(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=MAX_LENGTH)
