# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-13 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20170212_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trippicture',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
