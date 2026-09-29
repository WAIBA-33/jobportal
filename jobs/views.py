from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobForm
from .models import Job


@login_required
def create_job(request):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    try:
        company = request.user.company
    except Exception:
        return redirect("companies:company_profile")

    if request.method == "POST":

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.company = company

            job.save()

            return redirect(
                "jobs:create_job"
            )

    else:

        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {
            "form": form,
            "company": company,
        }
    )

@login_required
def edit_job(request, job_id):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        company=request.user.company
    )

    if request.method == "POST":

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            return redirect(
                "jobs:my_jobs"
            )

    else:

        form = JobForm(
            instance=job
        )

    return render(
        request,
        "jobs/edit_job.html",
        {
            "form": form,
            "job": job,
        }
    )


@login_required
def job_list(request):

    search_query = request.GET.get(
        "search",
        ""
    ).strip()

    employment_type = request.GET.get(
        "employment_type",
        ""
    ).strip()

    jobs = Job.objects.filter(
        status=Job.Status.OPEN
    )

    if search_query:

        jobs = jobs.filter(
            Q(title__icontains=search_query)
            | Q(required_skills__icontains=search_query)
            | Q(location__icontains=search_query)
            | Q(description__icontains=search_query)
        )

    if employment_type:

        jobs = jobs.filter(
            employment_type=employment_type
        )

    jobs = jobs.order_by(
        "-posted_at"
    )

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs,
            "search_query": search_query,
            "employment_type": employment_type,
            "employment_types": Job.EmploymentType.choices,
        }
    )


@login_required
def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job,
        }
    )


@login_required
def my_jobs(request):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    try:
        company = request.user.company
    except Exception:
        return redirect("companies:company_profile")

    jobs = Job.objects.filter(
        company=company
    ).order_by(
        "-posted_at"
    )

    return render(
        request,
        "jobs/my_jobs.html",
        {
            "jobs": jobs,
            "company": company,
        }
    )


@login_required
def close_job(request, job_id):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        company=request.user.company
    )

    if request.method == "POST":

        job.status = Job.Status.CLOSED
        job.save()

    return redirect(
        "jobs:my_jobs"
    )

