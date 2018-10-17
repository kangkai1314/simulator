# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testplatform', '0002_ratingrule'),
    ]

    operations = [
        migrations.CreateModel(
            name='RulePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testplatform.RatingRule')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testplatform.TestPoint')),
            ],
        ),
    ]