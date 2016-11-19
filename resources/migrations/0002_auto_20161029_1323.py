# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sermon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='resources.Sermon'),
        ),
    ]
