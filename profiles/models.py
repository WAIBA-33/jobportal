from django.conf import settings
from django.db import models


class JobSeekerProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_seeker_profile",
        limit_choices_to={"role": "JOB_SEEKER"},
    )

    full_name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15
    )

    location = models.CharField(
        max_length=200
    )

    skills = models.TextField(
        help_text="Enter your skills separated by commas."
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
    )

    education = models.CharField(
        max_length=200,
        blank=True,
    )

    preferred_job_type = models.CharField(
        max_length=20,
        blank=True,
    )

    preferred_location = models.CharField(
        max_length=200,
        blank=True,
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name