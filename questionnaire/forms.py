import datetime

import django
from django import forms

from questionnaire.models import Service


class BootstrapStylesMixin:
    fields = None
    textarea_rows = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.fields:
            for fieldname in self.fields:
                if isinstance(self.fields[fieldname], django.forms.DateField):
                    self.fields[fieldname].widget.years = reversed(
                        range(1901, datetime.date.today().year + 1)
                    )
                    self.fields[fieldname].widget.attrs["class"] = "form-select"
                    continue
                if hasattr(self.fields[fieldname], "choices"):
                    self.fields[fieldname].widget.attrs["class"] = "form-select"
                    continue
                if hasattr(self.fields[fieldname], "empty_label"):
                    self.fields[fieldname].empty_label = "выбрать..."
                    self.fields[fieldname].widget.attrs["class"] = "form-select"
                    continue
                class_object = self.fields[fieldname]
                if isinstance(class_object.widget, django.forms.widgets.Textarea):
                    self.fields[fieldname].widget.attrs["rows"] = self.textarea_rows
                if isinstance(class_object, django.forms.fields.BooleanField):
                    continue
                self.fields[fieldname].widget.attrs["class"] = "form-control"


class CreateServiceForm(BootstrapStylesMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "type",
            "title",
            "age",
            "weight",
            "height",
            "size",
            "nationality",
            "hair",
            "gender",
            "appearance",
            "location",
            "phone",
            "messanger",
            "call_time_start",
            "call_time_end",
            "price_half_hour",
            "price_one_hour",
            "price_two_hours",
            "price_full",
            "price_one_hour_outdoors",
            "price_two_hours_outdoors",
            "price_full_outdoors",
            "description",
            "additions",
            "video",
            "owner",
        ]
        help_texts = {"price_half_hour": "Укажите цену если оказываете экспресс услугу (30 мин)"}

    def clean(self):
        super().clean()
        a = '#'
