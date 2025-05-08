from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class College(models.Model):
    name = models.CharField(max_length=255)

class CustomUser(AbstractUser):
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ("Super Admin", "Super Admin"),
            ("College Admin", "College Admin"),
            ("Staff", "Staff"),
        ],
        default="Staff",
    )
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

class BellSchedule(models.Model):  # ✅ Ensure this class exists
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    time = models.TimeField()
    bell_type = models.CharField(max_length=50, choices=[("Normal", "Normal"), ("Exam", "Exam")])
    duration = models.IntegerField(default=5)
    is_bell_active = models.BooleanField(default=True)  # Allows Staff to toggle bells ON/OFF