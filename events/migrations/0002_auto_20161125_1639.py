# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-25 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, default='', max_length=3, null=True),
        ),
    ]