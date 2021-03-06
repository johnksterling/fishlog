# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_trip_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trips.Trip')),
            ],
        ),
    ]
