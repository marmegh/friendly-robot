# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User, Post, Comment
import bcrypt

# Create your views here.
def new(request):
    #start the journey
    register = RegistrationForm()
    return render(request, 'users/new.html', {'register': register})
def signin(request):
    #start the journey
    login = LoginForm()
    return render(request, 'users/login.html', {'login':login})
def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('users:new')
    else:
    #process registration form to add an account
        fname = request.POST['first']
        lname = request.POST['last']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpw = request.POST['cpw']
        hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        print hash1
        print bcrypt.checkpw(cpw.encode(), hash1)
        admin = User.objects.filter(user_level = 9)
        if admin.count() < 1:
            User.objects.create(first_name = fname, last_name = lname, email = email, user_level = 9, password = hash1)
        else:
            User.objects.create(first_name = fname, last_name = lname, email = email, user_level = 1, password = hash1)
        temp = User.objects.get(email = email)
        request.session['id'] = temp.id
        request.session['level'] = temp.user_level
        level = temp.user_level
        if level > 5:
            return redirect('/admin_dashboard')
        else:
            return redirect('/dashboard')
def login(request):
    # process login form
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('users:signin')
    else:
        email = request.POST['email']
        temp = User.objects.get(email = email)
        request.session['id'] = temp.id
        request.session['level'] = temp.user_level
        print request.session['id']
        level = temp.user_level
        if level > 5:
            return redirect('/admin_dashboard')
        else:
            return redirect('/dashboard')
def logout(request):
    del request.session['id']
    return redirect('/')
def show(request, user_id):
    context = {
        'id': request.session['id'],
        'user': User.objects.get(id=user_id),
        'posts': Post.objects.filter(user_id=user_id),
        'comments': Comment.objects.all(),
    }
    return render(request, 'users/profile.html', context)
def delete(request, user_id):
    user = User.objects.get(id=user_id)
    admin = User.objects.filter(user_level = 9)
    if admin.count() < 2 and user.user_level >5:
        return HttpResponse('Unable to delete final admin.')
    elif user.id == request.session['id']:
        user.delete()
        del request.session['id']
        return redirect('/')
    else:
        user.delete()
        return redirect('/admin_dashboard')
def edit(request, user_id):
    register = RegistrationForm()
    context = {
        'user': User.objects.get(id = user_id),
        'register': register,
    }
    level = request.session['level']
    if level > 5:
        return render(request, 'users/admin_edit.html', context)
    else:
        return render(request, 'users/edit.html', context)
def update(request):
    errors = User.objects.update_validator(request.POST)
    user_id = request.POST['user_id']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('users/edit/%s' %user_id)
    else:
        lvl = request.session['level']
        if lvl > 5:
            #process registration form to update an account
            fname = request.POST['first']
            lname = request.POST['last']
            email = request.POST['email']
            pwd = request.POST['pwd']
            cpw = request.POST['cpw']
            user_id = request.POST['user_id']
            hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
            print hash1
            print bcrypt.checkpw(cpw.encode(), hash1)
            temp = User.objects.get(id = user_id)
            desc = request.POST['desc']
            if desc > 1:
                temp.description = desc
                temp.save()
            if len(cpw)>0:
                if request.POST['user_level'] == 'admin':
                    level = 9
                else:
                    level = 1
                temp.first_name = fname
                temp.last_name = lname
                temp.email = email
                temp.user_level = level
                temp.password = hash1
                temp.save()
            else:
                temp.first_name = fname
                temp.last_name = lname
                temp.email = email
                temp.user_level = level
                temp.save()
            return redirect('/admin_dashboard')
        else:
            fname = request.POST['first']
            lname = request.POST['last']
            email = request.POST['email']
            pwd = request.POST['pwd']
            cpw = request.POST['cpw']
            desc = request.POST['desc']
            user_id = request.POST['user_id']
            hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
            temp = User.objects.get(id = user_id)
            if len(desc)>1:
                temp.description = desc
                temp.save()
            if len(cpw)>0:
                temp.first_name = fname
                temp.last_name = lname
                temp.email = email
                temp.password = hash1
                temp.save()
            else:
                temp.first_name = fname
                temp.last_name = lname
                temp.email = email
                temp.save()
            return redirect('/dashboard')

def post(request):
    post= request.POST['post']
    user_pk = request.POST['user_id']
    user_id= User.objects.get(id=user_pk)
    poster_pk = request.session['id']
    poster= User.objects.get(id=poster_pk)
    Post.objects.create(user = user_id, poster = poster, post = post)
    return redirect('/users/show%s' %user_pk)
def comment(request):
    comment = request.POST['comment']
    post_pk = request.POST['post_id']
    post = Post.objects.get(id=post_pk)
    commenter_pk = request.session['id']
    commenter= User.objects.get(id=commenter_pk)
    user_pk = request.POST['user_id']
    Comment.objects.create(commenter = commenter, post = post, comment = comment)
    return redirect('/users/show%s' %user_pk)