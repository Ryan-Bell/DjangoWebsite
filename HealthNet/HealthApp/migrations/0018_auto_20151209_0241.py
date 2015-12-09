# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0017_auto_20151208_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logitem',
            name='username',
        ),
        migrations.AddField(
            model_name='logitem',
            name='action',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='logitem',
            name='datetime',
            field=models.DateField(null=True),
        ),
    ]
