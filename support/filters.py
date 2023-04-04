import django_filters
from django import forms
from django.db.models import Q
from django_filters import CharFilter

from support.models import Support


class BootstrapStylesFiltersMixin:
    filters = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.filters:
            for fieldname in self.filters:
                class_object = self.filters[fieldname]
                if hasattr(self.filters[fieldname].field, "empty_label"):
                    self.filters[fieldname].field.empty_label = "выбрать..."
                    self.filters[fieldname].field.widget.attrs["class"] = "form-select"
                    continue
                if isinstance(class_object, forms.fields.BooleanField):
                    continue
                self.filters[fieldname].field.widget.attrs["class"] = "form-control"


class SupportTopicsFilter(BootstrapStylesFiltersMixin, django_filters.FilterSet):
    title_and_description = CharFilter(
        method="title_and_description_icontains", label="Поиск"
    )

    class Meta:
        model = Support
        fields = ["title_and_description"]

    def title_and_description_icontains(self, queryset, name, value):
        return queryset.filter(
            Q(topic__icontains=value) | Q(description__icontains=value)
        )
