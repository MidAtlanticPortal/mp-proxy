# from django.conf.urls import patterns, url, include
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    #'',
    # (r'^get_legend_json/(?P<url>)$', getLegendJSON),
    # instead retain compatibility with v2 client behavior
    re_path(r'^get_legend_json/', getLegendJSON),
    re_path(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
    path('events/get_filters', get_filters),
    re_path(r'^capabilities/(?P<layer_id>\d*)', capabilities_proxy_view),
]
