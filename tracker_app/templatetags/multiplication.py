from django import template

register = template.Library()

@register.simple_tag()
def multiply(a, b, *args, **kwargs):
    return a * b
