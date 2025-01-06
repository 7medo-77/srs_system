from django.db import models
from authentication.models.AuthUser import AuthUser
from grading.models.department import Department

# Create your models here.

class Student(models.Model):
  """
  Student class
  """
  student_id = models.AutoField(primary_key=True)
  date_of_birth = models.DateField()

  # Attributes relating to authUser class
  # first_name = models.CharField(max_length=255)
  # last_name = models.CharField(max_length=255)
  # email = models.EmailField(unique=True)
  # phone_number = models.CharField(max_length=20)

  major = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="major")
  user = models.OneToOneField(
    AuthUser,
    on_delete=models.CASCADE,
    related_name="student_profile",
  )

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()][1:])
    return attributes

  class Meta:
    db_table="students"