# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User
import bcrypt

# Create your views here.
def index(request):
    #start the journey
    login = LoginForm()
    register = RegistrationForm()
    return render(request, 'logreg/index.html', {'login':login, 'register': register})
def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        fname = request.POST['first']
        lname = request.POST['last']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpw = request.POST['cpw']
        hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        print hash1
        print bcrypt.checkpw(cpw.encode(), hash1)
        User.objects.create(first_name = fname, last_name = lname, email = email, password = hash1)
        temp = User.objects.get(email = email)
        request.session['id'] = temp.id
        return redirect('/dashboard')
    #process registration form to add an account
    print request.POST['first_name']
    return HttpResponse('testing registration')
def login(request):
    # process login form
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        email = request.POST['email']
        temp = User.objects.get(email = email)
        request.session['id'] = temp.id
        print request.session['id']
        return redirect('/dashboard')
def dashboard(request):
    id = request.session['id']
    user = User.objects.get(id = id)
    context = {
        'id':id,
        'name': user.first_name
    }
    return render(request, 'logreg/dashboard.html', context)
def logout(request):
    del request.session['id']
    return redirect('/')