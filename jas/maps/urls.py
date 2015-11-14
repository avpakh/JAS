from django.conf.urls import patterns, url, include
from maps.views import *



urlpatterns = [
    url(r'^$', 'maps.views.main',name='maps'),
 ]
