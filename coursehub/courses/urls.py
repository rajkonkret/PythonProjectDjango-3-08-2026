from django.urls import path
from . import views

app_name = "courses"
# courses:home

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.course_list, name="course_list"),
]
# ctrl alt l - formatowanie wg PEP8
