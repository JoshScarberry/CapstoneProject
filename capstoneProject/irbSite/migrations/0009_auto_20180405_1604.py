# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0008_project_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user_id',
            new_name='user',
        ),
    ]