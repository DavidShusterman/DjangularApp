# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='bussiness_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='story_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]