# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import Content, Image

# Create your views here.
def index(request, name):
    #
    # return render(request, 'index.html')
    content = Content.objects.get(name=name)
    images = Image.objects.filter(name=name).order_by('page')
    return render(request, 'index.html', {
        'base': 'http://7xlxrt.com1.z0.glb.clouddn.com',
        'content': content,
        'images': images,
    })


'''
def index2(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })'''
