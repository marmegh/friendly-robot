from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register', views.register, name = 'register'),
    url(r'^login', views.login, name = 'login'),
    url(r'^loggin', views.loggin, name = 'loggin'),
    url(r'^create', views.create, name = 'create'),
    url(r'^', views.index, name = 'index'),
]