from django.contrib import admin
from .models import Subject, Result


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "subject",
        "semester",
        "obtained_marks",
        "max_marks",
    )

    list_filter = ("semester", "subject")
    search_fields = (
        "student__name",
        "student__roll_no",
        "subject__name",
    )