import os
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from coltrane.feeds import CategoryFeed, LatestEntriesFeed
feeds = { 'entries': LatestEntriesFeed,
 		  'categories': CategoryFeed }

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^categories/', include('coltrane.urls.categories')),
	(r'^links/', include('coltrane.urls.links')),
	(r'^tags/', include('coltrane.urls.tags')),
	(r'^', include('coltrane.urls.entries')),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),
)

# this is for serving static files in development
if settings.DEBUG:
    urlpatterns += patterns('',
        (
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {
                'document_root': os.path.join(os.path.dirname(__file__), '../static')
            }
        ),
		(
			r'^yui/(?P<path>.*)$',
			'django.views.static.serve',
			{
				'document_root': '/Users/Shared/Sites/yui/build'
			}
		),
    )