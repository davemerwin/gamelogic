from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from gamelogic.story import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    
    url(r'^(?P<id>\d+)/edit/$', views.story_edit, name='story_edit'),
    url(r'^(?P<id>\d+)/$', views.story_detail, name='story_detail'),
    url(r'^$', views.story_list, name="story_list"),
)
