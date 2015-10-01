from django.db import models
from abc import ABCMeta, abstractclassmethod
# Create your models here.

class BaseUser(models.Model):
    #user = models.OneToOneField(user)
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def createAppointment(self): pass

    @abstractclassmethod
    def updateAppointment(self): pass

    @abstractclassmethod
    def cancelAppointment(self): pass

    @abstractclassmethod
    def updateUserInfo(self): pass

class Patient(BaseUser):
    MAX_LENGTH = 50

    #Basic Info
    firstName = models.CharField(max_length=MAX_LENGTH)
    middleName = models.CharField(max_length=MAX_LENGTH)
    lastName = models.CharField(max_length=MAX_LENGTH)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=2,
                                      choices=GENDER_CHOICES,
                                      default=MALE)
    dateBirth = models.DateField(verbose_name="Date of Birth")
    phonePrimary = models.CharField(max_length=MAX_LENGTH)
    phoneSecondary = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH)
    country = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)
    contactICEName = models.CharField(max_length=MAX_LENGTH)
    contactICERelationship = models.CharField(max_length=MAX_LENGTH)
    contactICEPhone = models.CharField(max_length=MAX_LENGTH)
    provider = models.CharField(max_length=MAX_LENGTH)
    #profileImage = models.ImageField(verbose_name="Profile Image")
        #cannot use imageField because pillow is not installed
    #disease Names and allergies w/ bool fields go here
