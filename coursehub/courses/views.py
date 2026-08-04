from django.db.models import Model
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

from .forms import CourseForm
from .models import Course


def home(request):
    # return HttpResponse("CourseHub - platforma szkoleniowa")
    return render(request, "courses/home.html")


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
def course_detail(request, pk):
    # course = Course.objects.filter(pk=pk)
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)

    return render(
        request,
        "courses/course_detail.html",
        {"course": course}
    )


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect(course)

    else:
        form = CourseForm()

    messages.success(request, 'Zmiany zapisane')
    return render(
        request,
        "courses/course_form.html",
        {"form": form},
    )
