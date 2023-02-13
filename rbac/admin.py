from django.contrib import admin


# app/admin.py
"""
PatientAdmin class defines the fields that should be displayed in the admin site when viewing a list of patients,
as well as the fields that can be searched using the admin site's search bar. 
NurseAdmin and AdminAdmin classes define the fields to display and search for nurses and admins, respectively. 
Once this code is added, the models can be managed using the Django admin site
"""

# app/admin.py

from django.contrib import admin
from .models import Patient, Nurse, Admin

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'medical_history')
    search_fields = ('name', 'medical_history')

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'years_of_experience')
    search_fields = ('name',)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

# --------------------------------------------

from django.contrib import admin
from .models import Patient, Nurse, Admin

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'years_of_experience')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Admin, AdminAdmin)

# --------------------------------------------
# Register your models here.

from django.contrib import admin
from rbac.models import User, Patient, Nurse, Admin

# Register the models for the admin site
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Admin)


# ---

from django.contrib import admin
from django.contrib.auth.models import User
from django_rbac.models import Role

# Define the different roles that users can have
ROLE_NAMES = ["patient", "nurse", "admin"]

# Create the roles if they don't already exist
for role_name in ROLE_NAMES:
    role, created = Role.objects.get_or_create(name=role_name)
    if created:
        print("Created role:", role_name)

# Assign users to their respective roles
patient_user = User.objects.get(username="patient_user")
nurse_user = User.objects.get(username="nurse_user")
admin_user = User.objects.get(username="admin_user")

patient_user.roles.add(Role.objects.get(name="patient"))
nurse_user.roles.add(Role.objects.get(name="nurse"))
admin_user.roles.add(Role.objects.get(name="admin"))
