# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class Projcet(models.Model):
    project_id=models.IntegerField(primary_key=True,unique=True,db_index=True)
    project_name=models.CharField(max_length=100)
    create_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name



class Task(models.Model):
    proj_id=models.ForeignKey(Projcet,related_name='project')
    task_id=models.IntegerField(primary_key=True,unique=True,blank=False,db_index=True)
    task_name=models.CharField(max_length=1000,blank=False,verbose_name='工单名称')
    task_type=models.IntegerField(blank=False)
    start_time=models.DateTimeField()
    end_time=models.DateField()
    status=models.IntegerField()

    def __str__(self):
        return self.task_name

    def __iter__(self):
        pass



class Case(models.Model):
    case_id=models.IntegerField(primary_key=True,unique=True,db_index=True)
    task_id=models.ForeignKey(to=Task,related_name='task_case')
    case_name=models.CharField(max_length=100,blank=False)
    create_time=models.DateField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return str(self.case_id)


class Function(models.Model):
    func_id=models.IntegerField(db_index=True,unique=True,blank=False)
    func_name=models.CharField(max_length=100)
    func_desc=models.TextField(max_length=100)

    def __str__(self):
        return str(self.func_id)


class Step(models.Model):
    case_id=models.ForeignKey(to=Case,related_name='case_step')
    step_order=models.IntegerField()
    func_id=models.ForeignKey(to=Function)
    step_name=models.CharField(max_length=100)

    def __str__(self):
        return self.step_name



class Menu(models.Model):
    menu_id=models.IntegerField(db_index=True,unique=True,blank=False)
    menu_name=models.CharField(max_length=100)


class Temlate(models.Model):
    temp_id=models.IntegerField(db_index=True,unique=True,blank=False)
    temp_name=models.CharField(max_length=100)


