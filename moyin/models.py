# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
    video_id=models.IntegerField(db_index=True,blank=False)
    video_name=models.CharField(max_length=100)
    video_desc=models.TextField()

    def __str__(self):
        return self.video_name

