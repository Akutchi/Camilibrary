from django import template

register = template.Library()

@register.filter
def clean_query (query):

    if query == "?filter=":
        return ""

    return query