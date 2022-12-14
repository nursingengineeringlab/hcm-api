# Design Doc:

The health management system with django rbac will have three user types: patient, nurse, and admin.
1. Patient User:
Can see the data of himself

Can update his own data

Cannot access the data of other patients

2. Nurse User:
Can see the data of a group of patients

Can update the data of the group of patients

Cannot access the data of other patients outside of the group

3. Admin User:
Can see all of the data

Can update all of the data

To implement this system, we will use the django-rbac package for role-based access control.
First, we will create the user models for each of the three user types. For the patient user, we will create a Patient model that extends the django-rbac User model. For the nurse user, we will create a Nurse model that extends the django-rbac User model. And for the admin user, we will create an Admin model that extends the django-rbac User model.

Next, we will create the PatientData model to store the data for each patient. This model will have fields for the patient's personal information, medical history, and current health status.

We will then create the PatientGroup model to store the group of patients that a nurse user has access to. This model will have a many-to-many relationship with the Patient model.

To implement the rbac permissions, we will create the PatientPermission, NursePermission, and AdminPermission classes. These classes will define the permissions for each user type, such as the ability to view and update their own data or the data of a group of patients.

Finally, we will create the views and templates for each user type to display and update their data.

Example Py Code:


from django.db import models 

from django_rbac.models import User 

  

class Patient(User): 

    # Patient user model that extends django-rbac User model 

    pass 

  

class Nurse(User): 

    # Nurse user model that extends django-rbac User model 

    pass 

  

class Admin(User): 

    # Admin user model that extends django-rbac User model 
