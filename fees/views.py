from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from .forms import FeeForm


def fee_list(request):
    fees = Fee.objects.all().order_by("-payment_date")

    return render(
        request,
        "fees/fee_list.html",
        {"fees": fees},
    )


def fee_add(request):

    if request.method == "POST":

        form = FeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("fee_list")

    else:
        form = FeeForm()

    return render(
        request,
        "fees/fee_add.html",
        {"form": form},
    )


def fee_edit(request, id):

    fee = get_object_or_404(Fee, id=id)

    if request.method == "POST":

        form = FeeForm(request.POST, instance=fee)

        if form.is_valid():
            form.save()
            return redirect("fee_list")

    else:
        form = FeeForm(instance=fee)

    return render(
        request,
        "fees/fee_edit.html",
        {
            "form": form,
            "fee": fee,
        },
    )


def fee_delete(request, id):

    fee = get_object_or_404(Fee, id=id)

    fee.delete()

    return redirect("fee_list")