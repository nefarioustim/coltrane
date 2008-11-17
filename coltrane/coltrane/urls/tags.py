from django.conf.urls.defaults import *
from coltrane.models import Entry, Link
from tagging.models import Tag

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': Tag.objects.all(),
															 'template_name': 'coltrane/tag_list.html'}, 'coltrane_tag_list'),
	(r'^entries/(?P<tag>[-\w]+)$', 'tagging.views.tagged_object_list', {'queryset_or_model': Entry.live.all(),
																		'template_name': 'coltrane/entries_by_tag.html'}, 'coltrane_tag_entry_detail'),
	(r'^links/(?P<tag>[-\w]+)$', 'tagging.views.tagged_object_list', {'queryset_or_model': Link,
																	  'template_name': 'coltrane/links_by_tag.html'}, 'coltrane_tag_link_detail'),
)