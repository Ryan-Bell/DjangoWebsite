# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0023_auto_20151209_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('doctor', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('description', models.CharField(max_length='200')),
            ],
        ),
    ]
