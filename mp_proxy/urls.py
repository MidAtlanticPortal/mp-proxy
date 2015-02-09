from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('',
    # (r'^get_legend_json/(?P<url>)$', getLegendJSON),
    # instead retain compatibility with v2 client behavior
    (r'^get_legend_json/', getLegendJSON),
    url(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
    url('events/get_filters', get_filters),
    url(r'^capabilities/(?P<layer_id>\d*)', capabilities_proxy_view),
)
