from django import template

register = template.Library()

@register.filter
def remove_last (query):

    query_list = query.split ("=")[1].split ("+")

    #  If query is of form www.camilibrary.fr/?filter=
    #  This may happen when deselecting every tag without clicking on "effacer"
    if len(query_list [:-2]) == 0:
        return ""

    return "?filter="+"+".join (query_list [:-2])