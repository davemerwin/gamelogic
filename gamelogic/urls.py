from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^(?P<slug>\d+)/edit/$', views.story_edit, name='story_edit'),
    url(r'^(?P<slug>\d+)/$', views.story_detail, name='story_detail'),
    url(r'^$', views.story_list, name="story_list"),
)
