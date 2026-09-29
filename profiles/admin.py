from django.contrib import admin

from .models import JobSeekerProfile


@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "user",
        "phone",
        "location",
        "preferred_job_type",
        "preferred_location",
        "created_at",
    )

    search_fields = (
        "full_name",
        "user__username",
        "phone",
        "location",
        "skills",
        "preferred_location",
    )

    list_filter = (
        "preferred_job_type",
        "location",
        "created_at",
    )

    ordering = (
        "-created_at",
    )