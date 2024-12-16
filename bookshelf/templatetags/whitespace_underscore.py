from django import template

register = template.Library()

@register.filter
def whitespace_underscore (value):
    return value.replace (" ", "_")