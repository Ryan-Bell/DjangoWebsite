# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0014_auto_20151205_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalinfo',
            name='otherText',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='city',
            field=models.CharField(max_length=50, default='none'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='eName',
            field=models.CharField(max_length=50, default='none'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='ePhoneNumber',
            field=models.CharField(max_length=50, default='none'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hospital',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
