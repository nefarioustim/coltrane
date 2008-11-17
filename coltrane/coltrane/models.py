import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.sites.models import Site
from django.db.models import signals
from django.utils.encoding import smart_str
from django.core.mail import mail_managers

from akismet import Akismet
from tagging.fields import TagField
from markdown import markdown

class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
	description = models.TextField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return ('coltrane_category_detail', (), { 'slug': self.slug })
	get_absolute_url = models.permalink(get_absolute_url)
	
	def live_entry_set(self):
		from coltrane.models import Entry
		return self.entry_set.filter(status=Entry.LIVE_STATUS)

class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
	)
	
	# Core fields
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	
	# Fields to store generate HTML
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html = models.TextField(editable=False, blank=True)
	
	# Metadata
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique_for_date='pub_date', help_text='Suggested value automatically generated from title. Must be unique.')
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, help_text="Only entries with 'Live' status will be publicly displayed.")
	
	# Categorisation
	categories = models.ManyToManyField(Category)
	tags = TagField()
	
	objects = models.Manager()
	live = LiveEntryManager()
	
	class Meta:
		ordering = ['-pub_date']
		verbose_name_plural = "Entries"
		
	def __unicode__(self):
		return self.title
	
	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save()
		
	def get_absolute_url(self):
		return ('coltrane_entry_detail', (), {"year": self.pub_date.strftime("%Y"),
											  "month": self.pub_date.strftime("%b").lower(),
											  "day": self.pub_date.strftime("%d"),
											  "slug": self.slug })
	get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
	url = models.URLField('URL', unique=True)
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	slug = models.SlugField(unique_for_date='pub_date', help_text='Suggested value automatically generated from title. Must be unique.')
	pub_date = models.DateTimeField('Published', default=datetime.datetime.now)
	posted_by = models.ForeignKey(User)
	description = models.TextField(blank=True, help_text='Optional.')
	description_html = models.TextField(editable=False, blank=True)
	enable_comments = models.BooleanField(default=True)
	post_elsewhere = models.BooleanField('Post to delicious.com', default=True, help_text='If checked, this link will be posted to both your blog and your delicious.com account.')
	via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person/site where you spotted the link. Optional.')
	via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')
	tags = TagField()
	
	class Meta:
		ordering = ['-pub_date']
	
	def __unicode__(self):
		return self.title
	
	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		if not self.id and self.post_elsewhere:
			import pydelicious
			from django.utils.encoding import smart_str
			pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD, smart_str(self.url), smart_str(self.title), smart_str(self.tags))
		super(Link, self).save()
	
	def get_absolute_url(self):
		return ('coltrane_link_detail', (), {"year": self.pub_date.strftime("%Y"),
											 "month": self.pub_date.strftime("%b").lower(),
											 "day": self.pub_date.strftime("%d"),
											 "slug": self.slug })
	get_absolute_url = models.permalink(get_absolute_url)

def moderate_comment(sender, **kwargs):
	comment = kwargs['comment']
	if not comment.id:
		entry = comment.content_object
		delta = datetime.datetime.now()-entry.pub_date
		if delta.days > 30:
			instance.is_public = False
		else:
			akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url="http:/%s/" % Site.objects.get_current().domain)
			if akismet_api.verify_key():
				akismet_data = {'comment_type': 'comment',
								'referrer': '',
								'user_ip': comment.ip_address,
								'user-agent': ''}
				if akismet_api.comment_check(smart_str(comment.comment), akismet_data,  build_data=True):
					comment.is_public = False
		email_body = "%s posted a new comment on the entry '%s'."
		mail_managers("New comment posted", email_body % (comment.person_name, comment.content_object))

comment_will_be_posted.connect(moderate_comment)