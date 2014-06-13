#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
        url(r'^all/$','article.views.articles'),
        url(r'^get/(?p<article_id>\d+)/$','article.views.article'),

)
