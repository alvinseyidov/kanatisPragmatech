from django import template
from ..models import Logo

def do_common_context(parser, token):
    return CommonNode()

class CommonNode(template.Node):
    def render(self, context):
        context['logo'] = Logo.objects.order_by('id').first()
        return ''

register = template.Library()
register.tag('get_common_models', do_common_context)