from django.urls import path
from . import views

urlpatterns = [
    path("", views.attendance_list, name="attendance_list"),
    path("add/", views.attendance_add, name="attendance_add"),
    path("edit/<int:id>/", views.attendance_edit, name="attendance_edit"),
    path("delete/<int:id>/", views.attendance_delete, name="attendance_delete"),
    path("add/", views.attendance_add, name="attendance_add"),
]