try:
    from django.urls import re_path, include
except ModuleNotFoundError as e:
    from django.conf.urls import url as re_path, include
# from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = [
    # (r'^get_legend_json/(?P<url>)$', getLegendJSON),
    # instead retain compatibility with v2 client behavior
    re_path(r'^get_legend_json/', getLegendJSON),
    re_path(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
    re_path('events/get_filters', get_filters),
    re_path(r'^capabilities/(?P<layer_id>\d*)', capabilities_proxy_view),
]
