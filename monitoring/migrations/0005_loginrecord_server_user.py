# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0004_serveruser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginrecord',
            name='server_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monitoring.ServerUser'),
            preserve_default=False,
        ),
    ]
