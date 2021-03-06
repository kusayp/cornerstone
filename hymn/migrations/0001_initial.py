# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-19 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Hymn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('has_refrain', models.BooleanField(default=False)),
                ('refrain', models.CharField(blank=True, max_length=1000, null=True)),
                ('categorys', models.ManyToManyField(blank=True, default=None, related_name='categorys', to='hymn.Category')),
            ],
            options={
                'verbose_name_plural': 'Hymns',
            },
        ),
        migrations.CreateModel(
            name='Stanza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('hymn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stanzas', to='hymn.Hymn')),
            ],
            options={
                'verbose_name_plural': 'Stanzas',
            },
        ),
    ]
