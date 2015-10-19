# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0006_auto_20151018_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tuberculosis', models.BooleanField(default=False)),
                ('influenza', models.BooleanField(default=False)),
                ('rheumatic', models.BooleanField(default=False)),
                ('whoopingCough', models.BooleanField(default=False)),
                ('tonsillitis', models.BooleanField(default=False)),
                ('measles', models.BooleanField(default=False)),
                ('mumps', models.BooleanField(default=False)),
                ('frequentColds', models.BooleanField(default=False)),
                ('germanMeasles', models.BooleanField(default=False)),
                ('scarletFever', models.BooleanField(default=False)),
                ('scarlatina', models.BooleanField(default=False)),
                ('diphtheria', models.BooleanField(default=False)),
                ('polio', models.BooleanField(default=False)),
                ('chickenpox', models.BooleanField(default=False)),
                ('coxsackie', models.BooleanField(default=False)),
                ('pneumonia', models.BooleanField(default=False)),
                ('highBloodPressure', models.BooleanField(default=False)),
                ('migraine', models.BooleanField(default=False)),
                ('strokes', models.BooleanField(default=False)),
                ('kidneyDisease', models.BooleanField(default=False)),
                ('arthritis', models.BooleanField(default=False)),
                ('allergy', models.BooleanField(default=False)),
                ('bleeding', models.BooleanField(default=False)),
                ('syphilis', models.BooleanField(default=False)),
                ('anemia', models.BooleanField(default=False)),
                ('obesity', models.BooleanField(default=False)),
                ('epilepsy', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='medicalInfo',
            field=models.OneToOneField(null=True, to='HealthApp.MedicalInfo'),
        ),
    ]
