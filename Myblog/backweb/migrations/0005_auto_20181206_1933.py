# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0004_auto_20181205_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('alias', models.CharField(max_length=20)),
                ('keywords', models.CharField(max_length=30, null=True)),
                ('describe', models.CharField(max_length=150)),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.Column')),
            ],
            options={
                'db_table': 'column',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backweb.Column'),
        ),
    ]
