from django import template

register = template.Library()


@register.filter(name='slice')
def slice(objects, slice):
    """Return objects from n1 to n2 from list"""
    n1 = int(slice.split()[0])
    n2 = int(slice.split()[1]) if slice.split()[1] != 'end' else -1
    return objects[int(slice.split()[0]):int(slice.split()[1])] if n2 != -1 else objects[int(slice.split()[0]):]
