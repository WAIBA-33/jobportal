from django import forms

from .models import JobSeekerProfile


class JobSeekerProfileForm(forms.ModelForm):

    class Meta:
        model = JobSeekerProfile

        fields = [
            "full_name",
            "phone",
            "location",
            "skills",
            "experience",
            "education",
            "preferred_job_type",
            "preferred_location",
            "resume",
        ]

        widgets = {
            "skills": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Python, Django, SQL, HTML, CSS"
                }
            ),
            "experience": forms.TextInput(
                attrs={
                    "placeholder": "e.g. 1 year"
                }
            ),
            "education": forms.TextInput(
                attrs={
                    "placeholder": "e.g. BCA"
                }
            ),
            "preferred_job_type": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Full Time"
                }
            ),
            "preferred_location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Kathmandu, Nepal"
                }
            ),
            "resume": forms.ClearableFileInput(
                attrs={
                    "accept": ".pdf,.doc,.docx"
                }
            ),
        }