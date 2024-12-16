from django import template

register = template.Library()

@register.filter
def extract_tag (value):
    return value.split("=")[1]