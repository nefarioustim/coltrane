from coltrane.models import Category, Entry, Link
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	
class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class LinkAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)

