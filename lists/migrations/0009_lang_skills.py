# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-27 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20200624_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='LANG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SKILLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(default='')),
            ],
        ),
    ]