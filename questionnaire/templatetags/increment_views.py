from django import template
from django.db.models import F

register = template.Library()


@register.simple_tag
def increment_views(service):
    """increase service views by 1"""
    service.views = F("views") + 1
    service.save(update_fields=["views"])
