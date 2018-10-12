#--*-- coding:utf-8 --*--
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^case/',views.case,name='case'),
    url(r'^index/',views.index,name='regress_index'),
    url(r'^project/',views.project,name='project')

]