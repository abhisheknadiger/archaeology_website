# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0004_auto_20171119_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='musuem',
        ),
        migrations.RemoveField(
            model_name='artifact_feedback',
            name='artifact',
        ),
        migrations.RemoveField(
            model_name='artifact_feedback',
            name='user',
        ),
        migrations.DeleteModel(
            name='Artifact',
        ),
        migrations.DeleteModel(
            name='artifact_feedback',
        ),
    ]