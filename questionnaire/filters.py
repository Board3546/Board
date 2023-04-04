import django_filters

from questionnaire.models import Service


class ServiceFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name="location", lookup_expr="iexact")
    price__gt = django_filters.NumberFilter(
        field_name="price_one_hour", lookup_expr="gt"
    )
    price__lt = django_filters.NumberFilter(
        field_name="price_one_hour", lookup_expr="lt"
    )
    age__gt = django_filters.NumberFilter(field_name="age", lookup_expr="gt")
    age__lt = django_filters.NumberFilter(field_name="age", lookup_expr="lt")

    class Meta:
        model = Service
        fields = ["location", "price_one_hour", "age"]
