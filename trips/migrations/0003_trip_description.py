# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20160703_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.CharField(default=datetime.datetime(2016, 7, 3, 12, 32, 12, 220687, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
