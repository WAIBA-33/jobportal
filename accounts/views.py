from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from profiles.models import JobSeekerProfile
from jobs.services import calculate_job_match
from .forms import RegistrationForm

from jobs.models import Job
from applications.models import Application


def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            messages.success(
                request,
                "Your account has been created successfully."
            )

            return redirect("accounts:login")

    else:

        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        }
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            if user.is_staff:

                return redirect("/admin/")

            if user.role == "EMPLOYER":

                return redirect("accounts:employer_dashboard")

            return redirect("accounts:job_seeker_dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


@login_required
def employer_dashboard(request):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    jobs = Job.objects.filter(
        company=request.user.company
    )

    total_jobs = jobs.count()

    open_jobs = jobs.filter(
        status=Job.Status.OPEN
    ).count()

    closed_jobs = jobs.filter(
        status=Job.Status.CLOSED
    ).count()

    total_applications = Application.objects.filter(
        job__company=request.user.company
    ).count()

    return render(
        request,
        "accounts/employer_dashboard.html",
        {
            "total_jobs": total_jobs,
            "open_jobs": open_jobs,
            "closed_jobs": closed_jobs,
            "total_applications": total_applications,
        }
    )


@login_required
def job_seeker_dashboard(request):

    if request.user.role != "JOB_SEEKER":
        return redirect("accounts:employer_dashboard")

    applications = Application.objects.filter(
        applicant=request.user
    )

    total_applications = applications.count()

    applied_applications = applications.filter(
        status=Application.Status.APPLIED
    ).count()

    shortlisted_applications = applications.filter(
        status=Application.Status.SHORTLISTED
    ).count()

    interview_applications = applications.filter(
        status=Application.Status.INTERVIEW
    ).count()

    selected_applications = applications.filter(
        status=Application.Status.SELECTED
    ).count()

    rejected_applications = applications.filter(
        status=Application.Status.REJECTED
    ).count()

    profile, created = JobSeekerProfile.objects.get_or_create(
        user=request.user
    )

    applied_job_ids = applications.values_list(
        "job_id",
        flat=True
    )

    jobs = Job.objects.filter(
        status=Job.Status.OPEN
    ).exclude(
        id__in=applied_job_ids
    )

    recommended_jobs = []

    for job in jobs:

        score = calculate_job_match(
            job,
            profile
        )

        recommended_jobs.append(
            {
                "job": job,
                "score": score,
            }
        )

    recommended_jobs.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    recommended_jobs = recommended_jobs[:5]

    return render(
        request,
        "accounts/job_seeker_dashboard.html",
        {
            "total_applications": total_applications,
            "applied_applications": applied_applications,
            "shortlisted_applications": shortlisted_applications,
            "interview_applications": interview_applications,
            "selected_applications": selected_applications,
            "rejected_applications": rejected_applications,
            "recommended_jobs": recommended_jobs,
        }
    )
@login_required
def user_logout(request):

    logout(request)

    return redirect("accounts:login")
