from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            "cover_letter",
        ]

        widgets = {
            "cover_letter": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": (
                        "Write a short cover letter explaining "
                        "why you are suitable for this job..."
                    ),
                }
            ),
        }