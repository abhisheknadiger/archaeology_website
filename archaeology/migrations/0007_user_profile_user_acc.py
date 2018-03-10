# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0006_artifact_artifact_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_acc',
            field=models.CharField(choices=[(1, 'visitor'), (2, 'archaeologist')], default=1, max_length=4),
        ),
    ]
