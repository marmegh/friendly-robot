from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^admin', views.admin, name = 'admin'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^', views.index, name = 'index'),
]