from django.shortcuts import render
from students.models import Student, Course
from fees.models import Fee

def home(request):
    context = {
        "student_count": Student.objects.count(),
        "courses": Course.objects.all(),
        "fee_count": Fee.objects.count(),
    }
    return render(request, "index.html", context)