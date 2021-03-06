# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regressplatform', '0005_auto_20181017_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='VueTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('name', models.IntegerField(db_index=True, unique=True)),
                ('province', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.IntegerField()),
                ('zip', models.CharField(max_length=200)),
            ],
        ),
    ]
