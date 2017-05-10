# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 22:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensor', '0011_auto_20170509_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot_data',
            name='rate',
        ),
        migrations.AddField(
            model_name='sections',
            name='rates',
            field=models.TextField(default=b'default_rates', verbose_name=b'Rates Array'),
        ),
        migrations.AddField(
            model_name='spot_data',
            name='occupant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
