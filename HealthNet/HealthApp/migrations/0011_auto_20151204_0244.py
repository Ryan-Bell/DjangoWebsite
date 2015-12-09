# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0010_auto_20151119_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50, blank=True)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField(blank=True)),
                ('zipcode', models.CharField(max_length=5)),
                ('phoneNumber', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('contactName', models.CharField(max_length=50)),
                ('contactPhoneNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('policyNumber', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
                ('groupNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='profileInfo',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='profileInfo',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='profileInfo',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='user',
        ),
        migrations.RenameField(
            model_name='medicalinfo',
            old_name='allergy',
            new_name='allergies',
        ),
        migrations.RenameField(
            model_name='medicalinfo',
            old_name='bleeding',
            new_name='migraines',
        ),
        migrations.RenameField(
            model_name='medicalinfo',
            old_name='migraine',
            new_name='rheumaticFever',
        ),
        migrations.RemoveField(
            model_name='medicalinfo',
            name='rheumatic',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='insuranceInfo',
        ),
        migrations.AlterField(
            model_name='patient',
            name='profileInfo',
            field=models.OneToOneField(to='HealthApp.ProfileInfo', null=True),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='InsuranceInfo',
        ),
        migrations.DeleteModel(
            name='Nurse',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='patient',
            name='userInfo',
            field=models.OneToOneField(to='HealthApp.UserInfo', null=True),
        ),
    ]
