# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0005_auto_20181206_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='father',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backweb.Column'),
        ),
    ]
