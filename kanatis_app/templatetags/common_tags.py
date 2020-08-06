from django import template
from ..models import Logo, AboutUs, Service

def do_common_context(parser, token):
    return CommonNode()

class CommonNode(template.Node):
    def render(self, context):
        context['logo'] = Logo.objects.order_by('id').first()
        context['about'] = AboutUs.objects.order_by('id').first()
        context['allservices'] = Service.objects.order_by('-id').all()

        return ''

register = template.Library()
register.tag('get_common_models', do_common_context)