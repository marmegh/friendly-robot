# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'thing/survey.html')
def process(request):
    try:
        request.session['count']
    except:
        request.session['count'] = 1
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    try:
        request.POST['comment']
    except:
        request.session['comment'] = ' '
    else:
        request.session['comment'] = request.POST['comment']
    temp = request.session['count']
    request.session['count'] = temp + 1
    return redirect('/result')
def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count'],
    }
    return render(request, 'thing/result.html', context)
def reset(request):
    del request.session['count']