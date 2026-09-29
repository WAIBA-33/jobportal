from django.urls import path

from . import views


app_name = "profiles"


urlpatterns = [

    path(
        "job-seeker/",
        views.job_seeker_profile,
        name="job_seeker_profile",
    ),

]