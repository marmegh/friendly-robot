# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

def index(request):
    #initiate Ninja Gold and load html OR load html without changing session
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        date = datetime.now()
        for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            request.session[attr] = getattr(date, attr)
        activity = '{}/{}/{} {}:{}:{} - Started playing...'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'])
        request.session['activity'] = [activity,]
    context = {
        'activities': request.session['activity'],
        'gold': request.session['gold'],
        'length': len(request.session['activity'])-1
    }
    return render(request, 'ninja/index.html', context)
def farm(request):
    #generate between 10 and 20 gold at the farm
    temp = random.randint(10,20)
    request.session['gold'] = request.session['gold'] + temp
    date = datetime.now()
    for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
        request.session[attr] = getattr(date, attr)
    activity = '{}/{}/{} {}:{}:{} - Earned {} gold at the farm'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'], temp)
    placeholder = request.session['activity']
    placeholder.append(activity)
    request.session['activity'] = placeholder
    return redirect('/')
def cave(request):
    #generate between 5 and 10 gold at the cave
    temp = random.randint(5,10)
    request.session['gold'] = request.session['gold'] + temp
    date = datetime.now()
    for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
        request.session[attr] = getattr(date, attr)
    activity = '{}/{}/{} {}:{}:{} - Earned {} gold in a cave'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'], temp)
    placeholder = request.session['activity']
    placeholder.append(activity)
    request.session['activity'] = placeholder
    # request.session['activity'] = activity + placeholder    
    return redirect('/')
def house(request):
    #generate between 2 and 5 gold at the house
    temp = random.randint(2,5)
    request.session['gold'] = request.session['gold'] + temp
    date = datetime.now()
    for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
        request.session[attr] = getattr(date, attr)
    activity = '{}/{}/{} {}:{}:{} - Earned {} gold at the house...'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'], temp)
    placeholder = request.session['activity']
    placeholder.append(activity)
    request.session['activity'] = placeholder
    return redirect('/')
def casino(request):
    #win or lose between 0 and 50 gold at the casino
    temp = random.randint(0,50) #set the bet
    chance = random.randint(0,1) #house's number
    #check number against house's number
    if chance > 0:
        request.session['gold']+=temp
        date = datetime.now()
        for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            request.session[attr] = getattr(date, attr)
        activity = '{}/{}/{} {}:{}:{} - Won {} gold at the casino'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'], temp)
        placeholder = request.session['activity']
        placeholder.append(activity)
        request.session['activity'] = placeholder
    else:
        date = datetime.now()
        for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            request.session[attr] = getattr(date, attr)
        activity = '{}/{}/{} {}:{}:{} - Lost {} gold at the casino'.format(request.session['month'], request.session['day'], request.session['year'], request.session['hour'], request.session['minute'], request.session['second'], temp)
        placeholder = request.session['activity']
        placeholder.append(activity)
        request.session['activity'] = placeholder
        request.session['gold']-=temp
    if request.session['gold'] < 0:
        request.session['gold'] = 0
    return redirect('/')
def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')