# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HealthApp', '0005_auto_20151008_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=14)),
                ('dateOfBirth', models.DateField(blank=True)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='PatientProfile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
