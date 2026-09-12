from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse


from .models import Student
from .forms import StudentForm


# Student List
def student_list(request):
    search = request.GET.get("search", "")

    students = Student.objects.all()

    if search:
        students = students.filter(first_name__icontains=search)

    paginator = Paginator(students, 10)
    page = request.GET.get("page")

    students = paginator.get_page(page)

    return render(request, "students/student_list.html", {
        "students": students,
        "search": search,
    })


# Add Student
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {
        "form": form
    })


# Edit Student
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {
        "form": form
    })


# Delete Student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect("student_list")


# Export Excel
def export_excel(request):

    students = Student.objects.all()

    data = []

    for s in students:
        data.append({
            "Admission No": s.admission_number,
            "Roll No": s.roll_number,
            "Name": f"{s.first_name} {s.last_name}",
            "Course": s.course.name if s.course else "",
            "Department": s.department.name if s.department else "",
            "Semester": s.semester.semester if s.semester else "",
            "Mobile": s.mobile,
            "Email": s.email,
            "Status": s.status,
        })

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="students.xlsx"'

    df.to_excel(response, index=False)

    return response