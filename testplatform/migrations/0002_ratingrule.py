# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_id', models.IntegerField(db_index=True, unique=True)),
                ('rule_name', models.CharField(max_length=100)),
            ],
        ),
    ]