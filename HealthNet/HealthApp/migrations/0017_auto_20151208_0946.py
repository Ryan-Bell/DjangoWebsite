# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0016_doctor_nurse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedTest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('released', models.BooleanField(default=False)),
                ('dateIssued', models.DateField()),
                ('result', models.TextField()),
                ('doctor', models.ForeignKey(to='HealthApp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('medicationCategory', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=50)),
                ('dosage', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('directions', models.TextField(max_length=50)),
                ('comments', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(null=True, to='HealthApp.Doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.ForeignKey(null=True, to='HealthApp.Hospital'),
        ),
        migrations.AddField(
            model_name='patient',
            name='prescriptions',
            field=models.ForeignKey(null=True, to='HealthApp.Prescription'),
        ),
    ]
