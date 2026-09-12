from django.urls import path
from . import views

urlpatterns = [
    path("", views.fee_list, name="fee_list"),
    path("add/", views.fee_add, name="fee_add"),
    path("edit/<int:id>/", views.fee_edit, name="fee_edit"),
    path("delete/<int:id>/", views.fee_delete, name="fee_delete"),
]