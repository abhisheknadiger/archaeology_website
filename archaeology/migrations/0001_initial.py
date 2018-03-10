# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 08:49
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buy_excavation_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_no', models.IntegerField(blank=True, null=True)),
                ('child_no', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buy_museum_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_no', models.IntegerField(blank=True, null=True)),
                ('child_no', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buy_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_no', models.IntegerField(blank=True, null=True)),
                ('child_no', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Excavation_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_ticket_rate', models.IntegerField(blank=True, null=True)),
                ('child_ticket_rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Excavations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('holiday', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='museum')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('holiday', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='museum')),
            ],
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('holiday', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='museum')),
            ],
        ),
        migrations.CreateModel(
            name='museum_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('musuem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archaeology.Museum')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Museum_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_ticket_rate', models.IntegerField(blank=True, null=True)),
                ('child_ticket_rate', models.IntegerField(blank=True, null=True)),
                ('museum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Museum')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('working_on', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_ticket_rate', models.IntegerField(blank=True, null=True)),
                ('child_ticket_rate', models.IntegerField(blank=True, null=True)),
                ('monument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Monument')),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('user_type', models.CharField(max_length=20, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='monument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monument', to='archaeology.Monument'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='excavation_ticket',
            name='excavation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Excavations'),
        ),
        migrations.AddField(
            model_name='buy_ticket',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Ticket'),
        ),
        migrations.AddField(
            model_name='buy_ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buy_museum_ticket',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Museum_ticket'),
        ),
        migrations.AddField(
            model_name='buy_museum_ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buy_excavation_ticket',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Excavation_ticket'),
        ),
        migrations.AddField(
            model_name='buy_excavation_ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='books',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archaeology.Library'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='musuem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archaeology.Museum'),
        ),
    ]
