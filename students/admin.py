from django.contrib import admin
from .models import Student, Department, Course, Semester

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Semester)