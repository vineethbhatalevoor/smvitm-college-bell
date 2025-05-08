from django.shortcuts import render, redirect
from .models import BellSchedule

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def menu(request):
    return render(request, "menu.html")  # ✅ Connects to menu.html template

def schedule(request):
    # ✅ Ensure user is authenticated, otherwise redirect to login
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        if request.user.role == "College Admin":
            bell_time = request.POST["time"]
            bell_type = request.POST["bell_type"]
            duration = 10 if bell_time in ["12:00", "16:40"] else 5
            BellSchedule.objects.create(college=request.user.college, time=bell_time, bell_type=bell_type, duration=duration)
        elif request.user.role == "Staff":
            # ✅ Allow Staff to toggle bell ON/OFF but not edit schedule
            bell = BellSchedule.objects.filter(college=request.user.college).first()
            if bell:
                bell.is_bell_active = not bell.is_bell_active
                bell.save()

    schedules = BellSchedule.objects.filter(college=request.user.college)
    return render(request, "schedule.html", {"schedules": schedules, "user_role": request.user.role})

def create_college_admin(request):
    # ✅ Ensure only Super Admins can create College Admins
    if request.user.is_authenticated and request.user.role == "Super Admin":
        if request.method == "POST":
            college_name = request.POST["college_name"]
            username = request.POST["username"]
            password = "college123"  # Default password (can be changed later)

            college, _ = College.objects.get_or_create(name=college_name)
            CustomUser.objects.create(
                username=username,
                password=make_password(password),
                college=college,
                role="College Admin"
            )

            return redirect("/admin/users/")  # ✅ Redirect to Django Admin Panel
    return render(request, "create_college_admin.html")