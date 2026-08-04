"""Tworzy dane demonstracyjne do ćwiczeń.

Uruchomienie:
    python manage.py seed_demo
"""
from datetime import date, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from courses.models import Course, Trainer


class Command(BaseCommand):
    help = "Tworzy przykładowych trenerów i kursy"

    def handle(self, *args, **options):
        anna, _ = Trainer.objects.get_or_create(
            email="anna.nowak@example.com",
            defaults={"first_name": "Anna", "last_name": "Nowak"},
        )
        jan, _ = Trainer.objects.get_or_create(
            email="jan.kowalski@example.com",
            defaults={"first_name": "Jan", "last_name": "Kowalski"},
        )

        examples = [
            ("Python od podstaw", Decimal("1290.00"), anna, 7),
            ("Django - aplikacje webowe", Decimal("1890.00"), jan, 14),
            ("REST API z Django", Decimal("1590.00"), jan, 21),
        ]
        for title, price, trainer, days in examples:
            Course.objects.get_or_create(
                title=title,
                defaults={
                    "description": f"Kurs demonstracyjny: {title}.",
                    "price": price,
                    "start_date": date.today() + timedelta(days=days),
                    "trainer": trainer,
                    "max_participiants": 12,
                },
            )
        self.stdout.write(self.style.SUCCESS("Dane demonstracyjne są gotowe."))
