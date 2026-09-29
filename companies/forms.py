from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = [
            "name",
            "description",
            "location",
            "website",
            "phone",
            "email",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe your company..."
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Kathmandu, Nepal"
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Company contact number"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "company@example.com"
                }
            ),
        }