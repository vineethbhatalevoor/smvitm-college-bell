from django.urls import path
from .views import index, schedule, about, create_college_admin

urlpatterns = [
    path("", index, name="home"),
    path("menu/", menu, name="menu"),
    path("schedule/", schedule, name="schedule"),
    path("about/", about, name="about"),
    path("create_college_admin/", create_college_admin, name="create_college_admin"),
]