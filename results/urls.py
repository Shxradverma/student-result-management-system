from django.urls import path
from . import views

urlpatterns = [
    path("", views.result_list, name="result_list"),
    path("add/", views.result_add, name="result_add"),
    path("edit/<int:id>/", views.result_edit, name="result_edit"),
    path("delete/<int:id>/", views.result_delete, name="result_delete"),
]