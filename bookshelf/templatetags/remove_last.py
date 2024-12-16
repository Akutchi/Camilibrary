from django import template

register = template.Library()

@register.filter
def remove_last (query):
    print(query)
    query_list = query.split ("=")[1].split ("+")
    return "?filter="+"+".join (query_list [:-2])