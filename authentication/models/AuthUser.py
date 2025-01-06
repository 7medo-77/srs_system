from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AuthUser(AbstractUser):
  user_role = [
    ( "admin", "Admin"),
    ( "instructor", "Instructor"),
    ( "student", "Student"),
  ]

  role = models.CharField(max_length=25, choices=user_role, default="student")
  phone_number = models.CharField(max_length=20)