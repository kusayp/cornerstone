# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='hymns',
        ),
        migrations.AddField(
            model_name='hymn',
            name='categorys',
            field=models.ManyToManyField(blank=True, default=None, related_name='categorys', to='hymn.Category'),
        ),
    ]
