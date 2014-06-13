from django.conf.urls import patterns, include, url
#from django.conf.urls.patterns()
#from django.conf.urls.url()
#from django.conf.urls.patterns()
#from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    (r'^articles/',include('article.urls')),
    
    #url(r'^hello/$','article.views.hello'),
    
    #url(r'^hello_template/$','article.views.hello_template'),
    #url(r'^hello_template_simple/$','article.views.hello_template_simple'),
    #url(r'^hello_clalss_view/$',HelloTemplate.as_view()),
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
