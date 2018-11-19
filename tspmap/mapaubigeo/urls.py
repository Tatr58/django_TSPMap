from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.viewMap, name='viewMap'),
    re_path(r'^cp_filter/$', views.filter_cp, name='cp_filter'),
]