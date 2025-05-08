from django.contrib import admin
from django.urls import path, include  # ✅ Include function required

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Admin Panel
    path("", include("bell_system.urls")),  # ✅ Link app URLs
]