# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request,'courselist/index.html', context)
def destroy(request, entry_id):
    context = {
        'course' : Course.objects.get(id=entry_id)
    }
    return render(request, 'courselist/confirm.html', context)
def deletion(request, entry_id):
    temp = Course.objects.get(id=entry_id)
    temp.delete()
    return redirect('/')
def create(request):
    print request.POST['name']
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')