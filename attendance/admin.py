from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "date",
        "status",
    )

    search_fields = (
        "student__name",
        "student__roll_no",
    )

    list_filter = (
        "date",
        "status",
    )