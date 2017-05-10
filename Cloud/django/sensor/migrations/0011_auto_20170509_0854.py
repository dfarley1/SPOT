# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0010_sections_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sections',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='spot_data',
            name='occupant',
        ),
        migrations.AddField(
            model_name='spot_data',
            name='rate',
            field=models.FloatField(null=True, verbose_name=b'Rate'),
        ),
    ]