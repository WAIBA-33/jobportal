from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    role = forms.ChoiceField(
        choices=[
            (User.Role.EMPLOYER, "Employer"),
            (User.Role.JOB_SEEKER, "Job Seeker"),
        ],
        widget=forms.RadioSelect,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "role",
            "password1",
            "password2",
        ]