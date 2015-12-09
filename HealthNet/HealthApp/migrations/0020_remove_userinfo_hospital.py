# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0019_nurse_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='hospital',
        ),
    ]
