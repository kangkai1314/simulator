# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestPoint(models.Model):
    test_id=models.IntegerField(db_index=True,unique=True,blank=False)
    type=models.CharField(max_length=100,default='normal')
    value=models.CharField(max_length=100)

    def __str__(self):

        return self.type+self.value

class RatingRule(models.Model):
    rule_id=models.IntegerField(db_index=True,unique=True,blank=False)
    rule_name=models.CharField(max_length=100)

    def __str__(self):
        return self.rule_name

class RulePoints(models.Model):
    rule_id=models.ForeignKey(RatingRule)
    test_id=models.ForeignKey(TestPoint)


