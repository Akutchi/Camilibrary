from django import template

register = template.Library()

@register.filter
def has_tag (query, tag):

    if query == "":
        return False

    return tag in query.split("=")[1].split("+")