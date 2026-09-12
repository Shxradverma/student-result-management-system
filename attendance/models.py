from django.db import models
from students.models import Student


class Attendance(models.Model):
    STATUS = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Leave", "Leave"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="Present"
    )

    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"