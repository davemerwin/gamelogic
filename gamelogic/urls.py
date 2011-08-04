from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gamelogic.story import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    
    url(r'^(?P<id>\d+)/edit/$', views.story_edit, name='story_edit'),
    url(r'^(?P<id>\d+)/$', views.story_detail, name='story_detail'),
    url(r'^$', views.story_list, name="story_list"),
)

urlpatterns += staticfiles_urlpatterns()
    
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/dynamic/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )