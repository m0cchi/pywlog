from django import template
import markdown

from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def gfm(value):
    return markdown.markdown(value, ['gfm'])
