# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0017_auto_20180406_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_submitted',
            field=models.DateField(auto_now=True),
        ),
    ]
