# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0008_auto_20151119_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
    ]
