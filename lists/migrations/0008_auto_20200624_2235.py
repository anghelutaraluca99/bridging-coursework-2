# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20200624_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='institution',
            new_name='qualification',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='title',
            new_name='school',
        ),
    ]