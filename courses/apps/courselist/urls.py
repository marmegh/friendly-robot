from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'destroy/(?P<entry_id>[0-9])', views.destroy),
    url(r'deletion/(?P<entry_id>[0-9])', views.deletion),
    url(r'addition', views.create),
    url(r'^', views.index),
]