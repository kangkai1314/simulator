# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regressplatform', '0003_auto_20181009_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.IntegerField(db_index=True, unique=True)),
                ('menu_name', models.CharField(max_length=100)),
            ],
        ),
    ]
