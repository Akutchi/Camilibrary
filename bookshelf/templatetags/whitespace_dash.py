from django import template

register = template.Library()

@register.filter
def whitespace_dash (value):
    return value.replace (" ", "-")