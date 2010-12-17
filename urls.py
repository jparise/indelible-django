from django.conf.urls.defaults import *

from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.static import serve

import feeds, settings, sitemaps

admin.autodiscover()

sitemaps = {
    'static':   sitemaps.StaticSitemap,
    'ink':      sitemaps.InkSitemap,
}

urlpatterns = patterns('',
    (r'^ink/',                  include('ink.urls')),
    (r'^admin/doc/',            include('django.contrib.admindocs.urls')),
    (r'^admin/ink/',            include('ink.admin_urls')),
    (r'^admin/(.*)',            admin.site.root),
    (r'^feeds/ink/((?P<category>.*)\.xml)?$', feeds.FreshInk()),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                                {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^m/(?P<path>.*)$', serve,
            {'document_root': 'media', 'show_indexes': False})
    )

urlpatterns += patterns('',
    url(r'^projects/$', direct_to_template, {'template': 'projects.html'}),
    url(r'^feeds/$',    direct_to_template, {'template': 'feeds.html'}),
    url(r'^about/$',    direct_to_template, {'template': 'about.html'}),
    url(r'^$',          direct_to_template, {'template': 'index.html'}),
)
