# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0012_auto_20151205_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='userInfo',
            field=models.ForeignKey(to='HealthApp.UserInfo', null=True),
        ),
    ]
