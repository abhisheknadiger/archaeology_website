# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 17:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archaeology', '0005_auto_20171119_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='museum')),
                ('musuem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archaeology.Museum')),
            ],
        ),
        migrations.CreateModel(
            name='artifact_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archaeology.Artifact')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]