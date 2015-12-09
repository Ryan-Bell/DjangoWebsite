# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0021_auto_20151209_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitem',
            name='datetime',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='logitem',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
