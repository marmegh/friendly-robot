from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add', views.add, name = 'add'),
    url(r'^create', views.create, name = 'create'),
    url(r'^delete/(?P<review_id>[0-9])', views.delete, name = 'delete'),
    url(r'^review', views.review, name = 'review'),
    url(r'^(?P<book_id>[0-9])', views.book, name = 'book'),
]