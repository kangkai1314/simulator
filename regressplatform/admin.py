# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

class TaskAdmin(admin.ModelAdmin):
    list_filter = ['task_id','task_type','status']


class StepAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Task,TaskAdmin)
admin.site.register(models.Case)
admin.site.register(models.Step)
admin.site.register(models.Function)
admin.site.register(models.Projcet)
admin.site.register(models.Menu)
admin.site.register(models.Temlate)
admin.site.register(models.VueTemplate)

