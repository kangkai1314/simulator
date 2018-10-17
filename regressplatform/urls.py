#--*-- coding:utf-8 --*--
from . import views
from django.conf.urls import url,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'task',views.TaskViewSet)

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^case/$',views.case,name='case'),
    url(r'^index/',views.index,name='regress_index'),
    url(r'^project/',views.project,name='project'),
    url(r'^task/',views.task,name='task'),
    url(r'^tasks/', views.tasks, name='tasks'),
    url(r'^ajax/',views.ajax,name='ajax'),

    url(r'^case_detail/',views.case_detail,name='case_detail'),
    url(r'^case/(?P<case_id>\d)/$', views.case_details,name='case_details'),


    url(r'^framework/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^template/',views.template,name='template')

]