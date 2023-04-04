from django import template

register = template.Library()


@register.simple_tag
def has_followed(user, service_id):
    """Check if current user is followed this service"""
    return user.profile.favorites.filter(id=service_id).exists()
