from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rbac.models import User, Patient, Nurse, Admin

class RBACTests(TestCase):
    def setUp(self):
        # create users
        self.patient = User.objects.create(username="patient1", user_type="patient")
        self.nurse = User.objects.create(username="nurse1", user_type="nurse")
        self.admin = User.objects.create(username="admin1", user_type="admin")
        # create patients
        self.patient1 = Patient.objects.create(user=self.patient, name="patient1")
        self.patient2 = Patient.objects.create(user=self.patient, name="patient2")
        # create nurse with assigned patients
        self.nurse1 = Nurse.objects.create(user=self.nurse, name="nurse1")
        self.nurse1.patients.add(self.patient1, self.patient2)


def test_patient_data_access(self):
    # patient can only access own data
    self.assertTrue(self.patient1.can_access(self.patient))
    self.assertFalse(self.patient1.can_access(self.nurse))
    self.assertFalse(self.patient1.can_access(self.admin))

def test_nurse_data_access(self):
    # nurse can access assigned patients' data
    self.assertTrue(self.patient1.can_access(self.nurse))
    self.assertTrue(self.patient2.can_access(self.nurse))
