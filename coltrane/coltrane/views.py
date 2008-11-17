from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response, get_object_or_404
from coltrane.models import Entry
from coltrane.models import Category

def entries_index(request):
	return render_to_response("coltrane/entry_index.html",
								{"object_list": Entry.live.all()})

def category_detail(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return object_list(request, queryset=category.live_entry_set(), extra_context={"category": category})