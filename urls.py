from django.conf.urls.defaults import *

from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic.simple import direct_to_template
from django.views.static import serve

import feeds, settings

admin.autodiscover()

feeds = {
    'ink':  feeds.FreshInk,
}

urlpatterns = patterns('',
    (r'^ink/',                  include('ink.urls')),
    (r'^projects/',             include('projects.urls')),
    (r'^admin/doc/',            include('django.contrib.admindocs.urls')),
    (r'^admin/ink/',            include('ink.admin_urls')),
    (r'^admin/(.*)',            admin.site.root),
    (r'^feeds/(?P<url>.*)(/|\.xml)$', 'django.contrib.syndication.views.feed',
                                {'feed_dict': feeds}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^m/(?P<path>.*)$', serve,
            {'document_root': 'media', 'show_indexes': False})
    )

urlpatterns += patterns('',
    url(r'^feeds/$',    direct_to_template, {'template': 'feeds.html'}),
    url(r'^about/$',    direct_to_template, {'template': 'about.html'}),
    url(r'^$',          direct_to_template, {'template': 'index.html'}),
)
