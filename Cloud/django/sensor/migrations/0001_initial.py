# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spot_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_uuid', models.UUIDField()),
                ('section', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='spot_status',
            fields=[
                ('sensor_uuid', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('occ_status', models.SmallIntegerField(default=0)),
                ('occ_since', models.DateTimeField()),
                ('occ_license', models.CharField(max_length=20)),
            ],
        ),
    ]