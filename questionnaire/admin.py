from django.contrib import admin

from questionnaire.models import MultipleImage, Service, Category, Addition, Review, \
    OnTopPrice

admin.site.register(Service)
admin.site.register(MultipleImage)
admin.site.register(Category)
admin.site.register(Addition)
admin.site.register(Review)
admin.site.register(OnTopPrice)

