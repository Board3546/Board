from django.contrib import admin

from support.models import Support, Ticket, SiteReview


# Register your models here.
class SupportAdmin(admin.ModelAdmin):
    list_display = ("topic", "slug", "id", "short_description")
    list_display_links = ("topic", "slug", "id")
    list_filter = ("topic", "slug", "id")
    search_fields = ("topic", "description")


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "status",
        "user",
        "short_question",
        "short_answer",
        "id",
        "created_at",
    )
    list_display_links = ("short_question", "user", "slug")
    list_filter = ("status", "user", "id")
    search_fields = ("question", "user")


class SiteReviewAdmin(admin.ModelAdmin):
    list_display = ("created_by", "rate", "id", "comment", "wishes")
    list_display_links = ("rate", "created_by", "comment", "wishes")
    list_filter = ("rate", "id", "created_by")
    search_fields = ("comment", "wishes", "created_by")


admin.site.register(Support, SupportAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(SiteReview, SiteReviewAdmin)
