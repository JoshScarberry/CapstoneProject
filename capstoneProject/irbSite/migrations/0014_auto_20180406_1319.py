# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0013_auto_20180406_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.AutoField(default=11, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
