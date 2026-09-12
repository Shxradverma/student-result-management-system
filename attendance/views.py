from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm
from django.shortcuts import get_object_or_404


def attendance_list(request):
    attendance = Attendance.objects.all().order_by("-date")

    return render(
        request,
        "attendance/attendance_list.html",
        {"attendance": attendance},
    )


def attendance_add(request):

    if request.method == "POST":
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")

    else:
        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_add.html",
        {"form": form},
    )
from django.shortcuts import render, redirect, get_object_or_404

def attendance_edit(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")
    else:
        form = AttendanceForm(instance=attendance)

    return render(
        request,
        "attendance/attendance_add.html",
        {"form": form},
    )



def attendance_add(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")

    else:
        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_add.html",
        {"form": form},
    )

def attendance_delete(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == "POST":
        attendance.delete()
        return redirect("attendance_list")

    return render(
        request,
        "attendance/attendance_delete.html",
        {
            "attendance": attendance
        }
    )