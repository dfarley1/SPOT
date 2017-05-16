# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20170505_0026'),
    ]

    operations = [
        migrations.DeleteModel(
            name='parking_rates',
        ),
        migrations.AddField(
            model_name='event_log',
            name='total_paid',
            field=models.IntegerField(default=0, verbose_name=b'Total charge'),
        ),
    ]
