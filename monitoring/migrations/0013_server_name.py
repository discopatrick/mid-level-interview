# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0012_make_loginrecord_server_not_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]