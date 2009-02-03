from django.contrib.sitemaps import Sitemap, GenericSitemap
from ink.models import Entry

class StaticSitemap(Sitemap):
    changefreq = 'monthly'

    pages = {
        'about':    '/about/',
        'feeds':    '/feeds/',
        'projects': '/projects/',
    }

    def items(self):
        return self.pages.keys()

    def location(self, obj):
        return self.pages[obj]

class InkSitemap(Sitemap):
    changefreq = 'never'

    def items(self):
        return Entry.public.all()

    def lastmod(self, obj):
        return obj.pub_date
