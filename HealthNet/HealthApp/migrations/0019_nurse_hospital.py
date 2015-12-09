# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0018_auto_20151209_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='hospital',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
