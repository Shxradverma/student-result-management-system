from django.contrib import admin
from django.urls import path, include
from config.views import home
from dashboard.views import admin_dashboard

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),

    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
    path("attendance/", include("attendance.urls")),
    path("notices/", include("notices.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("fees/", include("fees.urls")),
    path("results/", include("results.urls")),
]