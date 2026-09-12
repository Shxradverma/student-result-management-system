from django import forms
from .models import Fee


class FeeForm(forms.ModelForm):

    class Meta:
        model = Fee

        fields = [
            "student",
            "amount",
            "payment_date",
            "payment_status",
            "remarks",
        ]

        widgets = {

            "student": forms.Select(attrs={
                "class": "form-select"
            }),

            "amount": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "payment_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "payment_status": forms.Select(attrs={
                "class": "form-select"
            }),

            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

        }