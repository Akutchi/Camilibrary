from django import template

register = template.Library()

@register.filter
def not_empty_add (query, value):

    return query if query == "?filter=" else query+value