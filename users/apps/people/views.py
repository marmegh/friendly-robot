# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.db.models import Q

# Create your views here.
def index(request):
    context = {
        "users":User.objects.all(),
    }
    return render(request, 'people/index.html', context)
def new(request):
    return render(request,'people/creator.html')
def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request,'people/editor.html', context)
def show(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request,'people/display.html', context)
def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')
def create(request):
    print request.POST['fname']
    print request.POST['lname']
    print request.POST['email']
    User.objects.create(age = 1, first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'])
    return redirect('/users')
def confirm(request, user_id):
    print request.POST['fname']
    print request.POST['lname']
    print request.POST['email']
    temp = User.objects.get(id=user_id)
    temp.first_name = request.POST['fname']
    temp.last_name = request.POST['lname']
    temp.email = request.POST['email']
    temp.save()
    return redirect('/users')
