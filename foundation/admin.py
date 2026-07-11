from django.contrib import admin

from .models import Inquiry, Partner, SiteSettings


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "kind", "email", "created_at", "handled")
    list_filter = ("kind", "handled", "created_at")
    search_fields = ("full_name", "email", "message")
    readonly_fields = ("kind", "full_name", "email", "phone", "message", "details", "created_at")
    list_editable = ("handled",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Contact", {"fields": ("contact_email", "contact_phone", "address")}),
        ("Social links", {"fields": ("facebook_url", "instagram_url", "linkedin_url")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "website")
    list_display_links = ("name",)
    list_editable = ("order",)
