# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        #!!!!!Check if user already exists!!!
        emailsearch = User.objects.filter(email = postData['email'])
        if len(emailsearch)>0:
            errors['email'] = 'Account already exists'
        #ensure first and last name contain only letters
        if not re.match(r'^[a-zA-Z]+$', postData['first']):
            errors['first'] = 'First name can only contain letters'
        if not re.match(r'^[a-zA-Z]+$', postData['last']):
            errors['last'] = 'Last name can only contain letters'
        #check if first name is at least one character long
        if len(postData['first'])<1:
            errors['first'] = "First name required"
        #check that passwords match
        if len(postData['pwd']) < 8:
            errors['password_length'] = "Passwords must be at least 8 characters long"
        if postData['pwd'] != postData['cpw']:
            errors['password'] = "Confirmation did not match password"
        #check if last name is at least two characters long
        if len(postData['last'])<2:
            errors['last'] = "Last name too short"
        if len(postData['last'])<1:
            errors['last'] = "Last name required"
        return errors
    def update_validator(self,postData):
        errors = {}
        #!!!!!Check if user already exists!!!
        #ensure first and last name contain only letters
        if not re.match(r'^[a-zA-Z]+$', postData['first']):
            errors['first'] = 'First name can only contain letters'
        if not re.match(r'^[a-zA-Z]+$', postData['last']):
            errors['last'] = 'Last name can only contain letters'
        #check if first name is at least one character long
        if len(postData['first'])<1:
            errors['first'] = "First name required"
        #check if last name is at least two characters long
        if len(postData['last'])<1:
            errors['last'] = "Last name required"
        elif len(postData['last'])<2:
            errors['last'] = "Last name too short"
        #check that passwords match
        if postData['pwd'] != postData['cpw']:
            errors['password'] = "Confirmation did not match password"
        if postData['pwd'] < 8 and postData['pwd'] > 0:
            errors['password'] = "Passwords must be at least 8 characters long"
        return errors
    def login_validator(self,postData):
        errors = {}
        #check if user exists
        email = postData['email']
        emailsearch = User.objects.filter(email = email)
        if len(emailsearch) < 1:
            errors['email']='User not found'
        #verify password
        else:
            pwd = postData['pwd']
            temp = User.objects.get(email = email)
            hashedpw = temp.password
            if not bcrypt.checkpw(pwd.encode(), hashedpw.encode()):
                errors['password']='Unable to authenticate'
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    user_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts")
    poster = models.ForeignKey(User, related_name="postings")
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments")
    commenter = models.ForeignKey(User, related_name="commentings")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)