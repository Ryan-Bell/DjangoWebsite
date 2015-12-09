# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0011_auto_20151204_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileinfo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profileinfo',
            name='contactName',
        ),
        migrations.RemoveField(
            model_name='profileinfo',
            name='contactPhoneNumber',
        ),
        migrations.RemoveField(
            model_name='profileinfo',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='profileinfo',
            name='state',
        ),
    ]
