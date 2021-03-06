# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 02:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0003_auto_20171116_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(blank=True, error_messages={'invalid': 'Please enter your name'}, max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
