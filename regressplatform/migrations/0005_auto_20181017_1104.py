# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regressplatform', '0004_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_id', models.IntegerField(db_index=True, unique=True)),
                ('temp_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=1000, verbose_name='\u5de5\u5355\u540d\u79f0'),
        ),
    ]