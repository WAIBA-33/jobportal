from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CompanyForm
from .models import Company


@login_required
def company_profile(request):

    if request.user.role != "EMPLOYER":
        return redirect("accounts:job_seeker_dashboard")

    company, created = Company.objects.get_or_create(
        employer=request.user
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():

            company = form.save(
                commit=False
            )

            company.employer = request.user

            company.save()

            return redirect(
                "companies:company_profile"
            )

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        "companies/company_profile.html",
        {
            "form": form,
            "company": company,
            "created": created,
        }
    )