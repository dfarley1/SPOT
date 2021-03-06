# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parking_rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name=b'Start time')),
                ('end_time', models.TimeField(verbose_name=b'End time')),
                ('days', models.IntegerField(default=0, verbose_name=b'Days')),
                ('section', models.CharField(max_length=20, verbose_name=b'Section(s)')),
                ('spot', models.IntegerField(verbose_name=b'SPOT(s)')),
                ('rate', models.IntegerField(verbose_name=b'Rate per hour')),
            ],
        ),
    ]
