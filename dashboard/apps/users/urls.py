from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'show(?P<user_id>[0-9])', views.show, name = 'show'),
    url(r'delete/(?P<user_id>[0-9])', views.delete, name = 'delete'),
    url(r'update', views.update, name = 'update'),
    url(r'edit/(?P<user_id>[0-9])', views.edit, name = 'edit'),
    url(r'^create', views.create, name = 'create'),
    url(r'^login', views.login, name = 'login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^new', views.new, name = 'new'),
    url(r'^signin', views.signin, name = 'signin'),
    url(r'^comment', views.comment, name = 'comment'),
    url(r'^post', views.post, name = 'post'),
]