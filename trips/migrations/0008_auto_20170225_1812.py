# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-25 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20170213_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trippicture',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
    ]