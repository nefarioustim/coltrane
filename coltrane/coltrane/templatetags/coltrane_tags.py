from django.db.models import get_model
from django import template

def do_latest_content(parser, token):
	bits = token.contents.split()
	if len(bits) != 5:
		raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly four arguments.")
	model_args = bits[1].split('.')
	if len(model_args) != 2:
		raise template.TemplateSyntaxError("First argument to 'get_latest_content' must be an 'application name'.'model name' string.")
	model = get_model(*model_args)
	if model is None:
		raise template.TemplateSyntaxError("'get_latest_content' tag got an invalid model: %s" % bits[1])
	return LatestEntriesNode(model, bits[2], bits[4])

class LatestEntriesNode(template.Node):
	def __init__(self, model, num, varname):
		self.model = model
		self.num = num
		self.varname = varname
	def render(self, context):
		manager = self.model._default_manager
		if self.model.__name__ == 'Entry':
			manager = self.model.live
		context[self.varname] = manager.all()[:self.num]
		return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)