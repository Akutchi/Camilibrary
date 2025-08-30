from django import template

register = template.Library()

@register.filter
def add_last(to, filename):

    file_path = filename.split('/')

    print(filename + ' ' + ', '.join(file_path) + ' ' + to)
    
    return to + file_path[-1]
