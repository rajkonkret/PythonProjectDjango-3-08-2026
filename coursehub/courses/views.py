from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

from .forms import CourseForm
from .models import Course, Enrollment


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
        print(request.POST.dict())
        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            course = form.save()
            messages.success(request, 'Zmiany zapisane')
            return redirect(course)

    else:
        form = CourseForm()
        messages.success(request, 'Problem')

    return render(
        request,
        "courses/course_form.html",
        {"form": form},
    )

@login_required
def enroll_in_course(request, pk):
    if request.method == "POST":
        course = get_object_or_404(Course, pk=pk)

        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user, course=course
        )

        if created:

            messages.success(
                request,
                f"Pomyślnie zapisałeś się na kurs: {course.title}"
            )
        else:
            messages.warning(
                request,
                "Jestes juz zapisany na ten kurs."
            )
        redirect(course)  # dziąl dzieki get_absolute_url

    return redirect("courses:course_list")
