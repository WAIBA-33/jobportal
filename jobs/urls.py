from django.urls import path

from . import views


app_name = "jobs"


urlpatterns = [

    path(
        "create/",
        views.create_job,
        name="create_job",
    ),

    path(
        "",
        views.job_list,
        name="job_list",
    ),

    path(
    "<int:job_id>/",
    views.job_detail,
    name="job_detail",
    ),

    path(
    "my-jobs/",
    views.my_jobs,
    name="my_jobs",
    ),

    path(
    "close/<int:job_id>/",
    views.close_job,
    name="close_job",
    ),

    path(
    "edit/<int:job_id>/",
    views.edit_job,
    name="edit_job",
    ),

]