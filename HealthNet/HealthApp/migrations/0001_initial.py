# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('identfier', models.CharField(max_length=50, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dateBirth', models.DateField(verbose_name='Date of Birth')),
                ('phonePrimary', models.CharField(max_length=50)),
                ('phoneSecondary', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contactICEName', models.CharField(max_length=50)),
                ('contactICERelationship', models.CharField(max_length=50)),
                ('contactICEPhone', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
