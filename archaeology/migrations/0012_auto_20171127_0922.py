# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0011_auto_20171126_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='Abstract',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='publication',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
