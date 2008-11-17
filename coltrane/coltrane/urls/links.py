from django.conf.urls.defaults import *
from coltrane.models import Link

link_info_dict = {
	'queryset': Link.objects.all(),
	'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'^$', 'archive_index', link_info_dict, 'coltrane_link_archive_index'),
	(r'^(?P<year>\d{4})/$', 'archive_year', link_info_dict, 'coltrane_link_archive_year'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', link_info_dict, 'coltrane_link_archive_month'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', link_info_dict, 'coltrane_link_archive_day'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', link_info_dict, 'coltrane_link_detail'),
)