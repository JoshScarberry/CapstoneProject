# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0008_auto_20180421_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_complete',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No, allow submitter to edit')], default=True),
        ),
    ]
