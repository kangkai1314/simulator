# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import TestPoint,RatingRule,RulePoints

# Register your models here.

admin.site.register(TestPoint)
admin.site.register(RatingRule)
admin.site.register(RulePoints)