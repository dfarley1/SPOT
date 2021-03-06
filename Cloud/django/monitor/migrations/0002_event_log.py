# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 22:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_spot_data_occupant'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(null=True, verbose_name=b'Arrival')),
                ('end', models.DateTimeField(null=True, verbose_name=b'Departure')),
                ('spot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spot_occupied', to='sensor.spot_data')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occupant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
