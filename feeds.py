from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from ink.models import Category, Entry

class FreshInk(Feed):
    feed_type = Atom1Feed
    title = 'Indelible Ink'

    title_template = 'feeds/ink_title.html'
    description_template = 'feeds/ink_description.html'

    def get_object(self, bits):
        if len(bits) > 1:
            raise FeedDoesNotExist
        if len(bits) == 1:
            if bits[0].endswith('.xml'):
                bits[0] = bits[0][:-4]
            return Category.objects.get(slug=bits[0])
        return None

    def subtitle(self, obj):
        if obj:
            return 'Fresh Ink (%s)' % obj.name
        return 'Fresh Ink'

    def link(self, obj):
        return '/ink/'

    def categories(self, obj):
        if obj:
            return (obj,)
        return Category.objects.all()

    def items(self, obj):
        query_set = Entry.public
        if obj:
            query_set = obj.public_entry_set
        return query_set.order_by('-pub_date')[:10]

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.pub_date

    def item_categories(self, item):
        return item.categories.all()

    def item_copyright(self, item):
        year = item.pub_date.year
        return 'Copyright (c) %d, %s' % (year, item.author.get_full_name())
