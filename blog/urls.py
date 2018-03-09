#!/usr/bin/python3
"""
    ----coding:utf-8----
    @Author   : sobo
    @Time     : 2018/3/8 下午2:50
    @Software : 
    @File     : urls.py

"""

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_lst'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
]
