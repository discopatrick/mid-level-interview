# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_loginrecord_server_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginrecord',
            name='user',
        ),
    ]
