# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-12 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180109_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
