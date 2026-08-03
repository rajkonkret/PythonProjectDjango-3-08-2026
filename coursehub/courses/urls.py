from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.home, name="home")
]
# ctrl alt l - formatowanie wg PEP8
