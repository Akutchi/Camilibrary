from django import template

register = template.Library()

@register.filter
def whitespace_character (value, char):
    return value.replace (" ", char)