# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0014_auto_20170511_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='rates',
            field=models.TextField(default=b'rates_default', verbose_name=b'Rates Array'),
        ),
    ]
