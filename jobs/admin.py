from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "location",
        "employment_type",
        "status",
        "deadline",
        "posted_at",
    )

    search_fields = (
        "title",
        "company__name",
        "location",
        "required_skills",
    )

    list_filter = (
        "employment_type",
        "status",
        "location",
    )

    ordering = (
        "-posted_at",
    )