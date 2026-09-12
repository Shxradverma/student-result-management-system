from django.db import models
from students.models import Student


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    semester = models.IntegerField()

    max_marks = models.IntegerField(default=100)
    obtained_marks = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    semester = models.IntegerField()
    max_marks = models.IntegerField(default=100)
    obtained_marks = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def percentage(self):
        return round((self.obtained_marks / self.max_marks) * 100, 2)

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 40:
            return "D"
        return "F"

    def result_status(self):
        return "Pass" if self.percentage() >= 40 else "Fail"

    def __str__(self):
        return f"{self.student} - {self.subject}"