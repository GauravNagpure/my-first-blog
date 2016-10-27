from django.conf.urls import url
from . import views
urlpatterns = patterns('',
(r'^$', direct_to_template, {'template' : 'a.html'}),
