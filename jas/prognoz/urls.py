from django.conf.urls import patterns, url, include
from prognoz.views import *



urlpatterns = [
    url(r'^$', 'prognoz.views.main',name='prognoz'),
    url(r'^setmap/',setmap_page),
    url(r'^results/$','prognoz.views.results',name='results'),
    url(r'^calc.html$','prognoz.views.post_form_upload',name='post_form_upload'),

]
