import datetime

from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from ink.models import Entry

class FreshInk(Feed):
    feed_type = Atom1Feed
    title = 'Indelible Ink'
    subtitle = 'Fresh Ink'
    link = 'http://www.indelible.org/ink/'

    title_template = 'feeds/ink_title.html'
    description_template = 'feeds/ink_description.html'

    def items(self):
        return Entry.public.order_by('-pub_date')[:5]

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.pub_date
