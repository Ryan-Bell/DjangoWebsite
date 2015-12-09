# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0020_remove_userinfo_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitem',
            name='action',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
