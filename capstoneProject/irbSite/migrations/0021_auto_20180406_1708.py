# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0020_auto_20180406_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_submitted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='review_type',
            field=models.CharField(blank=True, choices=[('exempt review', 'Exempt Review'), ('expedited review', 'Expedited Review'), ('full irb review', 'Full IRB Review')], max_length=20),
        ),
    ]
