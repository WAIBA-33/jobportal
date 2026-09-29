from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "employer",
        "location",
        "email",
        "created_at",
    )

    search_fields = (
        "name",
        "employer__username",
        "email",
        "location",
    )

    list_filter = (
        "location",
        "created_at",
    )