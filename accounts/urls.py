from django.urls import path

from . import views


app_name = "accounts"


urlpatterns = [

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "login/",
        views.user_login,
        name="login",
    ),

    path(
    "employer/dashboard/",
    views.employer_dashboard,
    name="employer_dashboard",
    ),

    path(
    "job-seeker/dashboard/",
    views.job_seeker_dashboard,
    name="job_seeker_dashboard",
    ),

    path(
    "logout/",
    views.user_logout,
    name="logout",
    ),

]