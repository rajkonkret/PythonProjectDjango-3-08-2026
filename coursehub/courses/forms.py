from django import forms
from .models import Course, Trainer


class Courseform(forms.ModelForm):
    """
    MoodelForm automatycznie wykorzystuje typy i walidacje modelu Course.
    """

    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "price",
            "start_date",
            "max_participiants",
            "trainer",
            "active"
        ]

        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "descripion": forms.Textarea(attrs={"rows": 5})
        }
