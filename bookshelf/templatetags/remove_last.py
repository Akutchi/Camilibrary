from django import template

register = template.Library()

@register.filter
def remove_last (query):

    query_list = query.split ("=")[1].split ("+")

    if len(query_list [:-2]) == 0:
        return ""

    return "?filter="+"+".join (query_list [:-2])