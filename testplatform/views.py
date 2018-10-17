# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import TestPoint


def test_points(request):
    return render(request,'testplatform/html/testpoints.html')
