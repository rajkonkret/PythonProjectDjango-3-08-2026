from django import forms
from .models import Course, Trainer


class CourseForm(forms.ModelForm):
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

    def clean_title(self):
        """Przykład walidacji pojedynczego pola."""
        title = self.cleaned_data['title'].string()
        if len(title) < 3:
            raise forms.ValidationError("Tytuł musi mieć co najmniej 3 znaki")


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', "last_name", "email", "bio"]
