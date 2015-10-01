# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0002_auto_20151001_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='dateBirth',
        ),
    ]
