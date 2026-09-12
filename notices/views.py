from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from .forms import NoticeForm


def notice_list(request):
    notices = Notice.objects.all().order_by("-publish_date")

    return render(
        request,
        "notices/notice_list.html",
        {"notices": notices},
    )


def notice_add(request):

    if request.method == "POST":
        form = NoticeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("notice_list")

    else:
        form = NoticeForm()

    return render(
        request,
        "notices/notice_add.html",
        {"form": form},
    )


def notice_edit(request, id):

    notice = get_object_or_404(Notice, id=id)

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)

        if form.is_valid():
            form.save()
            return redirect("notice_list")

    else:
        form = NoticeForm(instance=notice)

    return render(
        request,
        "notices/notice_edit.html",
        {
            "form": form,
            "notice": notice,
        },
    )


def notice_delete(request, id):

    notice = get_object_or_404(Notice, id=id)
    notice.delete()

    return redirect("notice_list")