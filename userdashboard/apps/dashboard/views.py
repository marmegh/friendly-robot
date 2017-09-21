# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import LoginForm, RegistrationForm

# Create your views here.
def index(request):
    #start the journey
    return render(request, 'dashboard/index.html')
def register(request):
    #render a form to register
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('Registration Collected')
    else:
        form = RegistrationForm()

    return render(request, '/dashboard/registration.html', {'form': form})
def create(request):
    #process registration form to add an account
    return HttpResponse('testing registration')
def loggin(request):
    #render a form to register
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('Registration Collected')
    else:
        form = RegistrationForm()

    return render(request, '/dashboard/registration.html', {'form': form})
def login(request):
    #process login form
    return HttpResponse('are we there yet?')
