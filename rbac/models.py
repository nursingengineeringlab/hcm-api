from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Patient model has fields for the patient's name, age, gender, and medical history, 
Nurse model has fields for the nurse's name, years of experience, and list of patients they are assigned to, 
Admin model has fields for the admin user's username and password.

These fields are defined using Django's field types, such as CharField and IntegerField, 
and can be used to store and retrieve data in the app's database.
"""

# app/models.py

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    patients = models.ManyToManyField(Patient)


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
