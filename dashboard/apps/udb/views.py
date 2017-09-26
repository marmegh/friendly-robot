# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from ..users.models import User

# Create your views here.
def index(request):
    #start the journey
    return render(request, 'udb/index.html')
def admin(request):
    #the admin's dashboard
    if request.session['level']<5:
        return redirect('/dashboard')
    else:
        id = request.session['id']
        user = User.objects.get(id = id)
        users = User.objects.all()
        context = {
            'id': id,
            'name': user.first_name,
            'users': users,
        }
        return render(request, 'udb/admin_dashboard.html', context)
def dashboard(request):
    #standard user's dashboard
    id = request.session['id']
    user = User.objects.get(id = id)
    users = User.objects.all()
    context = {
        'id': id,
        'name': user.first_name,
        'users': users,
    }
    return render(request, 'udb/dashboard.html', context)
def logout(request):
    del request.session['id']
    return redirect('/')