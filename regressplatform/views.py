# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .apps import RegressplatformConfig
from .models import Task,Projcet,Menu

# Create your views here.

def getfileds(model):
    task_lists = model.objects.values()
    cols = []
    for i in task_lists:
        for j in i:
            if j in cols:
                break
            cols.append(j)
    return cols


def index(request):
    menus=Menu.objects.all()
    tasks=Task.objects.all()
    cols=getfileds(Task)
    projects=Projcet.objects.all()
    #return render(request,'regress/html/index.html',{'app':RegressplatformConfig.name,'tasks':tasks,'projects':projects})
    return render(request,'regress/html/shouye.html',{'task_cols':cols,'tasks':tasks,'menus':menus})


def case(request):
    projects = Projcet.objects.all()
    menus = Menu.objects.all()
    return render(request,'regress/html/case.html',{'menus':menus,'projects':projects})

def project(request):
    projects=Projcet.objects.all()
    cols=getfileds(Projcet)
    print cols
    return render(request,'regress/html/project.html',{'projects':projects,'cols':cols})
