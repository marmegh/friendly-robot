# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author, Book_Author
from django.db.models import Q

# Create your views here.
def index():
    return HttpResponse('Something')
