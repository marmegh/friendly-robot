# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import messages
from ..users.models import User
from .models import Book, Review, Author
import bcrypt

# Create your views here.
def add(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'books/new.html', context)
def create(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/add')
    else:
        if request.POST['author'] > 0:
            author = Author.objects.get(id = request.POST['author'])
        else:
            name = request.POST['new_author']
            author = Author.objects.create(name = name)
        title = request.POST['title']
        review =  request.POST['review']
        rating = request.POST['rating']
        id = request.session['id']
        reviewer = User.objects.get(id = id)
        book = Book.objects.create(title = title, author = author)
        r = Review.objects.create(stars = rating, review = review, reviewer = reviewer, book = book)
        return redirect('/dashboard')
def book(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {
        'id': request.session['id'],
        'book': book,
        'reviews': Review.objects.filter(book = book),
    }
    return render(request, 'books/book.html', context)
def review(request):
    book_id = request.POST['book_id']
    review = request.POST['review']
    rating = request.POST['rating']
    id = request.session['id']
    reviewer = User.objects.get(id = id)
    book = Book.objects.get(id = book_id)
    Review.objects.create(stars = rating, review = review, reviewer = reviewer, book = book)
    return redirect('/dashboard')
def delete(request, review_id):
    review = Review.objects.get(id = review_id)
    review.delete()
    return redirect('/dashboard')