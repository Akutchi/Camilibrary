from django import template

register = template.Library()

@register.filter
def remove_tag_if_present (query, value):

    value = value.replace (" ", "-")
    query_list = query.split ("=")[1].split ("+")

    #  If query is of form www.camilibrary.fr/?filter=
    #  This may happen when deselecting every tag without clicking on "effacer"
    if len(query_list [:-1]) == 0:
        return ""

    Need_Removal = query_list.count (value) == 1

    if Need_Removal:
        query_list.remove (value)

    return "?filter="+"+".join (query_list)