from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Teacher
from .forms import TeacherForm



def teacher_list(request):

    search = request.GET.get("search", "")

    teachers = Teacher.objects.all()

    if search:
        teachers = teachers.filter(first_name__icontains=search)

    paginator = Paginator(teachers, 10)

    page = request.GET.get("page")

    teachers = paginator.get_page(page)

    return render(request, "teachers/teacher_list.html", {
        "teachers": teachers,
        "search": search,
    })
def teacher_add(request):

    if request.method == "POST":

        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("teacher_list")

    else:

        form = TeacherForm()

    return render(request, "teachers/teacher_form.html", {
        "form": form
    })


def teacher_edit(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":

        form = TeacherForm(request.POST, request.FILES, instance=teacher)

        if form.is_valid():

            form.save()

            return redirect("teacher_list")

    else:

        form = TeacherForm(instance=teacher)

    return render(request, "teachers/teacher_form.html", {
        "form": form
    })


def teacher_delete(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    teacher.delete()

    return redirect("teacher_list")