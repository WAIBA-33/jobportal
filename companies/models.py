from django.conf import settings
from django.db import models


class Company(models.Model):

    employer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company",
        limit_choices_to={"role": "EMPLOYER"},
    )

    name = models.CharField(
        max_length=150
    )

    description = models.TextField()

    location = models.CharField(
        max_length=200
    )

    website = models.URLField(
        blank=True
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name