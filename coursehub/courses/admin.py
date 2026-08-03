from django.contrib import admin
from .models import Course, Trainer

# Register your models here.

# admin.site.register(Course) # komentujemy po dodaniu dekoratora
admin.site.register(Trainer)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "trainer",
        "price",
        "start_date",
        "active"
    )

    list_filter = ("active", "start_date", "trainer")
    search_fields = ("title", "description", "trainer__last_name")

    list_select_related = ("trainer",)  # ominiecie problemu N + 1
