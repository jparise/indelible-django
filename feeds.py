import datetime

from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from tagging.models import TaggedItem
from ink.models import Entry

class FreshInk(Feed):
    feed_type = Atom1Feed
    title = 'Indelible Ink'

    title_template = 'feeds/ink_title.html'
    description_template = 'feeds/ink_description.html'

    def get_object(self, bits):
        if len(bits) > 1:
            raise FeedDoesNotExist
        if len(bits) == 1:
            return Entry.tag_set.get(name=bits[0])
        return None

    def subtitle(self, obj):
        if obj:
            return 'Fresh Ink (%s)' % obj.name
        return 'Fresh Ink'

    def link(self, obj):
        if obj:
            return '/ink/tags/' + obj.name
        return '/ink/'

    def items(self, obj):
        query_set = Entry.public
        if obj:
            query_set = TaggedItem.objects.get_by_model(query_set, obj)
        return query_set.order_by('-pub_date')[:5]

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.pub_date
