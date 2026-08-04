from django.urls import path
from . import views

app_name = "courses"
# courses:home

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/new/", views.course_create, name="course_create")
]
# ctrl alt l - formatowanie wg PEP8
