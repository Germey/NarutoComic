# coding:utf-8
from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    page = models.IntegerField(max_length=5)