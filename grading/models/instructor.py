from django.db import models
from grading.models.department import Department
from authentication.models.AuthUser import AuthUser

class Instructor(models.Model):
  instructor_id = models.AutoField(primary_key=True)

  # first_name = models.CharField(max_length=255)
  # last_name = models.CharField(max_length=255)
  # email = models.EmailField(unique=True)
  # phone_number = models.CharField(max_length=50)

  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="instructors")
  user = models.OneToOneField(
    AuthUser,
    on_delete=models.CASCADE,
    related_name="instructor_profile",
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
    db_table="instructors"