# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0009_auto_20180421_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=20),
        ),
    ]
