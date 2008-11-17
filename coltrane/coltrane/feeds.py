from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from coltrane.models import Category, Entry

current_site = Site.objects.get_current()

class LatestEntriesFeed(Feed):
	author_name = "%s" % current_site.domain
	copyright = "http://%s/about/copyright/" % current_site.domain
	description = "Latest entries posted to %s" % current_site.name
	feed_type = Atom1Feed
	item_copyright = "http://%s/about/copyright/" % current_site.domain
	item_author_name = "%s" % current_site.domain
	item_author_link = "http://%s/" % current_site.domain
	link = "/feeds/entries/"
	title = "%s: Latest entries" % current_site.name
	
	def items(self):
		return Entry.live.all()[:15]
	
	def item_pubdate(self, item):
		return item.pub_date
	
	def item_guid(self, item):
		return "tag:%s,%s:%s" % (current_site.domain, item.pub_date.strftime('%Y-%m-%d'), item.get_absolute_url())
	
	def item_categories(self, item):
		return [c.title for c in item.categories.all()]

class CategoryFeed(LatestEntriesFeed):
	def get_object(self, bits):
		if len(bits) != 1:
			raise ObjectDoesNotExist
		return Category.objects.get(slug__exact=bits[0])
	
	def title(self, obj):
		return "%s: Latest entries in category '%s'" % (current_site.name, obj.title)
		
	def description(self, obj):
		return "%s: Latest entries in category '%s'" % (current_site.name, obj.title)
		
	def link(self, obj):
		return obj.get_absolute_url()
		
	def items(self, obj):
		return obj.live_entry_set()[:15]