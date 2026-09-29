from django import forms

from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            "title",
            "description",
            "required_skills",
            "location",
            "employment_type",
            "salary_min",
            "salary_max",
            "experience_required",
            "deadline",
            "status",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Describe the job..."
                }
            ),
            "required_skills": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Python, Django, SQL, HTML, CSS"
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Kathmandu, Nepal"
                }
            ),
            "experience_required": forms.TextInput(
                attrs={
                    "placeholder": "e.g. 1-2 years"
                }
            ),
            "deadline": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "salary_min": forms.NumberInput(
                attrs={
                    "placeholder": "Minimum salary"
                }
            ),
            "salary_max": forms.NumberInput(
                attrs={
                    "placeholder": "Maximum salary"
                }
            ),
        }