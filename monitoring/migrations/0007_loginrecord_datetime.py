# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_remove_loginrecord_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginrecord',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 16, 22, 25, 752881)),
            preserve_default=False,
        ),
    ]
