# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-18 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user_attending', models.ManyToManyField(related_name='travel_attending', to='login_reg_app.User')),
                ('user_planned_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_travel', to='login_reg_app.User')),
            ],
        ),
    ]
