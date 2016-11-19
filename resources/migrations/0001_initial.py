# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 16:40
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
                'verbose_name_plural': 'Sermon categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Sermon comments',
            },
        ),
        migrations.CreateModel(
            name='Devotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('principle', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('categorys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='resources.Category')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='sermon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Sermon'),
        ),
    ]
