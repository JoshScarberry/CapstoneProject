# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-29 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0011_auto_20180426_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notes_to_submitter',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
