from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from jobs.models import Job

from .forms import ApplicationForm
from .models import Application


@login_required
def apply_for_job(request, job_id):

    if request.user.role != "JOB_SEEKER":
        return redirect("accounts:employer_dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        status=Job.Status.OPEN
    )

    if Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists():

        messages.warning(
            request,
            "You have already applied for this job."
        )

        return redirect(
            "jobs:job_detail",
            job_id=job.id
        )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST
        )

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.job = job
            application.applicant = request.user

            application.save()

            messages.success(
                request,
                "Your application has been submitted successfully."
            )

            return redirect(
                "jobs:job_detail",
                job_id=job.id
            )

    else:

        form = ApplicationForm()

    return render(
        request,
        "applications/apply.html",
        {
            "form": form,
            "job": job,
        }
    )


@login_required
def employer_applications(request, job_id):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        company=request.user.company
    )

    applications = Application.objects.filter(
        job=job
    ).select_related(
        "applicant"
    ).order_by(
        "-applied_at"
    )

    return render(
        request,
        "applications/employer_applications.html",
        {
            "job": job,
            "applications": applications,
        }
    )


@login_required
def update_application_status(request, application_id):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=request.user.company
    )

    if request.method == "POST":

        new_status = request.POST.get("status")

        valid_statuses = [
            choice[0]
            for choice in Application.Status.choices
        ]

        if new_status in valid_statuses:

            application.status = new_status
            application.save()

            messages.success(
                request,
                "Application status updated successfully."
            )

    return redirect(
        "applications:employer_applications",
        job_id=application.job.id
    )


@login_required
def my_applications(request):

    if request.user.role != "JOB_SEEKER":
        return redirect("accounts:employer_dashboard")

    applications = Application.objects.filter(
        applicant=request.user
    ).select_related(
        "job",
        "job__company"
    ).order_by(
        "-applied_at"
    )

    return render(
        request,
        "applications/my_applications.html",
        {
            "applications": applications,
        }
    )


@login_required
def withdraw_application(request, application_id):

    if request.user.role != "JOB_SEEKER":
        return redirect("accounts:employer_dashboard")

    application = get_object_or_404(
        Application,
        id=application_id,
        applicant=request.user
    )

    if request.method == "POST":

        application.status = Application.Status.WITHDRAWN
        application.save()

        messages.success(
            request,
            "Your application has been withdrawn successfully."
        )

    return redirect(
        "applications:my_applications"
    )
