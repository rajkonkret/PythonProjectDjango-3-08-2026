from django.db.models import Model
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Course


def home(request):
    return HttpResponse("CourseHub - platforma szkoleniowa")


def about(request):
    return HttpResponse("Strona z kursami by Radek")


def course_list(request):
    courses = Course.objects.filter(active=True)

    return render(
        request,
        "courses/course_list.html",
        {"courses": courses}
    )

# {{ ... }} wartośc/wyrażenia
# {% ... %} tag sterująca - komenda
# {# ... #} komentarz w template