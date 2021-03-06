# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20170516_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Payment Method Name')),
                ('purchase_price', models.FloatField(default=0.0, verbose_name=b'Purchase Price')),
                ('rate_modifier', models.FloatField(default=1.0, verbose_name=b'Rate Modifier')),
            ],
        ),
    ]
