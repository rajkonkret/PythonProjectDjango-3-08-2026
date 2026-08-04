from django.urls import path
from . import views

app_name = "courses"
# courses:home

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/new/", views.course_create, name="course_create"),
    path("courses/<int:pk>/enroll", views.enroll_in_course, name="enroll_in_course"),
    path("my-courses/", views.my_courses, name="my_courses"),
]
# ctrl alt l - formatowanie wg PEP8
