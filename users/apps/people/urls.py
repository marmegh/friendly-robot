from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^new$', views.new),
    url(r'^delete/(?P<user_id>[0-9])', views.delete),
    url(r'^show/(?P<user_id>[0-9])', views.show),
    url(r'^edit/(?P<user_id>[0-9])', views.edit),
    url(r'^confirm/(?P<user_id>[0-9])', views.confirm),
    url(r'^create$',views.create),
    url(r'^', views.index),
]