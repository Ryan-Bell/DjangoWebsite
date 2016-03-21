# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0025_auto_20151209_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profileInfo',
        ),
    ]
