# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .apps import RegressplatformConfig
from .models import Task,Projcet,Menu,Case,Step,Temlate,VueTemplate

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, GroupSerializer,TaskSerializer,VueTemplateSedializer
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
    cases=Case.objects.all()
    cols = getfileds(Case)
    return render(request,'regress/html/case.html',{'menus':menus,'projects':projects,'cases':cases,'cols':cols})

def case_details(request,case_id):
    print case_id
    case=get_object_or_404(Case,case_id=case_id)
    steps=Step.objects.filter(case_id=case_id)
    return render(request,'regress/html/case_view.html',{'case':case,'steps':steps})



def project(request):
    menus = Menu.objects.all()
    projects=Projcet.objects.all()
    cols=getfileds(Projcet)
    print cols
    return render(request,'regress/html/project.html',{'projects':projects,'cols':cols,'menus':menus})

def task(request):
    projects = Projcet.objects.all()
    menus = Menu.objects.all()
    tasks=Task.objects.all()
    return render(request,'regress/html/task.html',{'menus':menus,'projects':projects,'tasks':tasks})

def tasks(request):
    if request.method == 'GET':
        task_lists = Task.objects.all()
        serializer = TaskSerializer(task_lists, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        return response


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def vuetemplate(request):
    if request.method == 'GET':
        task_lists = Task.objects.all()
        serializer = TaskSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def case_detail(request):
    menus = Menu.objects.all()
    return render(request,'regress/html/case_detail.html',{'menus':menus})


def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'regress/html/home.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = VueTemplate.objects.all()
    serializer_class = VueTemplateSedializer


def ajax(request):

    return render(request, "regress/html/ajax.html")
def test_ajax(request):        #这次请求在处理ajax请求，
    print(request.GET)        #拿到数据，去处理
    return HttpResponse("Hello kris") #根据数据给回调函数返回个什么参数

def cal(request):
    print(request.POST)
    n1=int(request.POST.get("n1")) #取出这两个值
    n2=int(request.POST.get("n2"))
    ret = n1+n2                   #计算下
    return HttpResponse(ret)


def template(request):
    menus = Menu.objects.all()
    tempaltes=Temlate.objects.all()
    return render(request,'regress/html/template.html',{'menus':menus,'templates':tempaltes})

def result(request):
    return render(request,'regress/html/result.html')

