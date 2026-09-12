from django.shortcuts import render, redirect, get_object_or_404

from .models import Result
from .forms import ResultForm


def result_list(request):
    results = Result.objects.select_related(
        "student",
        "subject"
    ).all()

    return render(
        request,
        "results/result_list.html",
        {"results": results},
    )


def result_add(request):

    if request.method == "POST":

        form = ResultForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("result_list")

    else:
        form = ResultForm()

    return render(
        request,
        "results/result_add.html",
        {"form": form},
    )


def result_edit(request, id):

    result = get_object_or_404(Result, id=id)

    if request.method == "POST":

        form = ResultForm(
            request.POST,
            instance=result
        )

        if form.is_valid():
            form.save()
            return redirect("result_list")

    else:
        form = ResultForm(instance=result)

    return render(
        request,
        "results/result_edit.html",
        {
            "form": form,
            "result": result,
        },
    )


def result_delete(request, id):

    result = get_object_or_404(Result, id=id)
    result.delete()

    return redirect("result_list")