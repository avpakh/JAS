from django.conf.urls import patterns, url, include
from datadb.views import *


urlpatterns = [
    url(r'^$', 'datadb.views.list_status',name='get_data'),
    url(r'^map/',map_page),
    url(r'^tables/',table_page),
    url(r'^update/',update_page),
    url(r'^graphs/',graph_page),
    url(r'^request/',request_page),
    url(r'^(?P<pk>[0-9]+)/$', 'datadb.views.showdetail', name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', 'datadb.views.showtypes', name='analys'),
    url(r'^graph/(?P<pk>[0-9]+)/$', 'datadb.views.graphs_page', name='graphs'),

]
