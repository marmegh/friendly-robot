# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        authorsearch = Author.objects.filter(name = postData['new_author'])
        if len(authorsearch)>0:
            errors['author'] = 'Select author from menu'
        if postData['author'] == 0 and len(postData['new_author'])<1:
            errors['author'] = 'Author required'
        if len(postData['title'])<1:
            errors['title'] = 'Book title missing'
        if len(postData['review'])<1:
            errors['review'] = 'Review missing'
        return errors

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name = 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
class Review(models.Model):
    stars = models.IntegerField()
    review = models.CharField(max_length = 255)
    reviewer = models.ForeignKey('users.User', related_name = 'reviews')
    book = models.ForeignKey(Book, related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)