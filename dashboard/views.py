from django.shortcuts import render
from students.models import Student

def admin_dashboard(request):

    context = {
        "student_count": Student.objects.count(),
        "teacher_count": 25,
        "attendance": 95,
        "fee_collection": 850000,
    }

    return render(request, "dashboard/admin_dashboard.html", context)


def teacher_dashboard(request):
    return render(request, "dashboard/teacher_dashboard.html")


def student_dashboard(request):
    return render(request, "dashboard/student_dashboard.html")


def parent_dashboard(request):
    return render(request, "dashboard/parent_dashboard.html")