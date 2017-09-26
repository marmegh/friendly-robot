# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import signin

# Create your tests here.
class HomePageTest(TestCase):
    def test_login(self):
        found = resolve('/users/signin')
        self.assertEqual(found.func, signin)
    def test_page_returns_correct_html(self):
        request = HttpRequest()
        response = signin(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>User Dashboard Assignment</title>', html)
        self.assertTrue(html.endswith('</html>'))