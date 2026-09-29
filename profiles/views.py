from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import JobSeekerProfileForm
from .models import JobSeekerProfile


@login_required
def job_seeker_profile(request):

    if request.user.role != "JOB_SEEKER":
        return redirect("accounts:employer_dashboard")

    profile, created = JobSeekerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = JobSeekerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            profile = form.save(
                commit=False
            )

            profile.user = request.user

            profile.save()

            return redirect(
                "profiles:job_seeker_profile"
            )

    else:

        form = JobSeekerProfileForm(
            instance=profile
        )

    return render(
        request,
        "profiles/job_seeker_profile.html",
        {
            "form": form,
            "profile": profile,
            "created": created,
        }
    )