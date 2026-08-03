from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("CourseHub - platforma szkoleniowa")


def about(request):
    return HttpResponse("Strona z kursami by Radek")
