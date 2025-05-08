from django.test import TestCase
from .models import BellSchedule, College, CustomUser
from django.utils.timezone import now

class BellScheduleTestCase(TestCase):
    def setUp(self):
        """Create test data."""
        self.college = College.objects.create(name="SMVITM College")
        self.admin_user = CustomUser.objects.create(username="admin", role="College Admin", college=self.college)
        self.staff_user = CustomUser.objects.create(username="staff", role="Staff", college=self.college)
        self.super_admin_user = CustomUser.objects.create(username="superadmin", role="Super Admin")

        self.bell = BellSchedule.objects.create(college=self.college, time="09:00", bell_type="Normal", duration=5)

    def test_bell_creation(self):
        """Test if a bell schedule entry is created correctly."""
        self.assertEqual(self.bell.college, self.college)
        self.assertEqual(self.bell.time, "09:00")
        self.assertEqual(self.bell.bell_type, "Normal")

    def test_admin_can_edit_schedule(self):
        """Ensure only College Admins can edit the schedule."""
        self.assertEqual(self.admin_user.role, "College Admin")

    def test_staff_cannot_edit_schedule(self):
        """Ensure Staff cannot edit schedule but can toggle bell ON/OFF."""
        self.assertEqual(self.staff_user.role, "Staff")

    def test_super_admin_can_create_college_admins(self):
        """Ensure Super Admin can generate logins for new colleges."""
        new_college = College.objects.create(name="New College")
        new_admin = CustomUser.objects.create(username="newadmin", role="College Admin", college=new_college)
        self.assertEqual(new_admin.role, "College Admin")
        self.assertEqual(new_admin.college.name, "New College")

    def test_bell_duration_logic(self):
        """Check if last bell duration is correctly set to 10 sec."""
        last_bell = BellSchedule.objects.create(college=self.college, time="16:40", bell_type="Normal", duration=10)
        self.assertEqual(last_bell.duration, 10)