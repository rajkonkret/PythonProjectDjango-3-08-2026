from django.urls import path
from . import views

app_name = "courses"
# courses:home

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
# ctrl alt l - formatowanie wg PEP8
