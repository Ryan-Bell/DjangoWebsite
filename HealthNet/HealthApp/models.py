from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from abc import ABCMeta, abstractclassmethod


class Patient(AbstractBaseUser):
    user = models.OneToOneField(User)
    MAX_LENGTH = 50
    identifier = models.EmailField(max_length=MAX_LENGTH, unique=True)
    USERNAME_FIELD = 'identifier'

    firstName = models.CharField(max_length=MAX_LENGTH)
    middleName = models.CharField(max_length=MAX_LENGTH)
    lastName = models.CharField(max_length=MAX_LENGTH)
    addressNumber = models.IntegerField(verbose_name="Street Number")
    addressStreet = models.CharField(max_length=MAX_LENGTH)
    addressCity = models.CharField(max_length=25)
    addressState = models.CharField(max_length=2)
    addressZip = models.IntegerField(verbose_name="Zip Code")
    phone = models.IntegerField(verbose_name="Phone Number")
    dob = models.DateField(verbose_name="Date of Birth")
    sex = models.CharField(max_length=20, verbose_name="Sex")
    contactName = models.CharField(max_length=MAX_LENGTH, verbose_name="Emergency Contact Name")
    contactRelationship = models.CharField(max_length=MAX_LENGTH, verbose_name="Emergency Contact Relationship")
    contactPhone = models.IntegerField(verbose_name="Emergency Contact Phone Number")

    tuberculosis = models.BooleanField()
    influenza = models.BooleanField()
    rheumatic = models.BooleanField()
    whoopingCough = models.BooleanField()
    tonsillitis = models.BooleanField()
    measles = models.BooleanField()
    mumps = models.BooleanField()
    frequentColds = models.BooleanField()
    germanMeasles = models.BooleanField()
    scarletFever = models.BooleanField()
    scarlatina = models.BooleanField()
    diphtheria = models.BooleanField()
    polio = models.BooleanField()
    chickenpox = models.BooleanField()
    coxsackie = models.BooleanField()
    pneumonia = models.BooleanField()

    diabetes = models.BooleanField()
    dtype = ''
    if diabetes:
        type = models.IntegerField(verbose_name="Type")

    cancer = models.BooleanField()
    ctype = ''
    if cancer:
        type = models.CharField(max_length=MAX_LENGTH, verbose_name="Type of Cancer")

    highBloodPressure = models.BooleanField()
    migraine = models.BooleanField()
    strokes = models.BooleanField()
    kidneyDisease = models.BooleanField()
    arthritis = models.BooleanField()
    allergy = models.BooleanField()
    bleeding = models.BooleanField()
    syphilis = models.BooleanField()
    anemia = models.BooleanField()
    obesity = models.BooleanField()
    epilepsy = models.BooleanField()

    is_declined = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = [firstName,lastName, addressNumber,
                       addressStreet, addressCity, addressState,
                       addressZip, phone, dob, sex, contactName,
                       contactRelationship, contactPhone]
