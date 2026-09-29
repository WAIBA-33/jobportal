from django.urls import path

from . import views


app_name = "applications"


urlpatterns = [

    path(
        "apply/<int:job_id>/",
        views.apply_for_job,
        name="apply_for_job",
    ),

    path(
    "employer/<int:job_id>/",
    views.employer_applications,
    name="employer_applications",
    ),

    path(
    "update-status/<int:application_id>/",
    views.update_application_status,
    name="update_application_status",
    ),

    path(
    "my-applications/",
    views.my_applications,
    name="my_applications",
    ),

    path(
    "withdraw/<int:application_id>/",
    views.withdraw_application,
    name="withdraw_application",
    ),

]