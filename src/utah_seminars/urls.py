from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'signups.views.home', name='home'),
     url(r'^talks', 'signups.views.talks', name='talks'),
     url(r'^twitter-signup', 'signups.views.twittersignups', name='twittersignups'),
     url(r'^create-talk', 'signups.views.createtalk', name='createtalk'),
     url(r'^sample-talk', 'signups.views.sampletalk', name='sampletalk'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)