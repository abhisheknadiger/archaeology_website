# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0002_publications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publications',
            new_name='Publication',
        ),
    ]
