# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-22 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190719_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(default='non-user.png', max_length=20),
        ),
    ]