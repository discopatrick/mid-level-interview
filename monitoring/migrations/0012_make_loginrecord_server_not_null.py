# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0011_loginrecord_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrecord',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.Server'),
        ),
    ]