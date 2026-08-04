from django.db import models
from django.urls import reverse


# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)  # dla pól tekstowych preferujemy blank

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
        # <Trainer: Anna Kowalska>


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # decimal
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    active = models.BooleanField(default=True)
    max_participiants = models.PositiveIntegerField(default=20)

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.PROTECT,  # nie mozemy skasowac trenera jesli istnieje przypisany do niego kurs
        related_name="courses"
    )

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"pk": self.pk})
# CASCADE, PROTECT, SET_NULL, RESTRICT
# relacja 1:n
# Trener 1 ----> N Course
# python .\manage.py makemigrations
# python .\manage.py migrate
# Operations to perform:
#  python .\manage.py showmigrations
