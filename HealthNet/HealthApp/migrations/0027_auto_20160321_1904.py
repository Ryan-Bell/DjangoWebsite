# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0026_remove_doctor_profileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='LogItem',
        ),
    ]
