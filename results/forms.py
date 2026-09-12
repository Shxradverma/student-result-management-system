from django import forms
from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = [
            "student",
            "subject",
            "semester",
            "max_marks",
            "obtained_marks",
        ]

        widgets = {
            "student": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.Select(attrs={"class": "form-select"}),
            "semester": forms.NumberInput(attrs={"class": "form-control"}),
            "max_marks": forms.NumberInput(attrs={"class": "form-control"}),
            "obtained_marks": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        max_marks = cleaned_data.get("max_marks")
        obtained_marks = cleaned_data.get("obtained_marks")

        if (
            max_marks is not None
            and obtained_marks is not None
            and obtained_marks > max_marks
        ):
            raise forms.ValidationError(
                "Obtained Marks cannot be greater than Max Marks."
            )

        return cleaned_data