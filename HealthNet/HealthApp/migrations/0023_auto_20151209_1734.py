# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0022_auto_20151209_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitem',
            name='datetime',
            field=models.DateField(null=True),
        ),
    ]
