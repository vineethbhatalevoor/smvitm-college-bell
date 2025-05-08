from django.contrib import admin
from .models import College, CustomUser, BellSchedule  # ✅ Ensure BellSchedule is imported

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "role", "college")

class BellScheduleAdmin(admin.ModelAdmin):
    list_display = ("college", "time", "bell_type", "duration", "is_bell_active")

admin.site.register(College)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BellSchedule, BellScheduleAdmin)