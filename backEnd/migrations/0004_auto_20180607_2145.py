# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backEnd', '0003_auto_20180607_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, to='backEnd.User'),
        ),
    ]
