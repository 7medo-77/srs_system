from django.db import models
from Department.model import Department

# Create your models here.

class Student(models.Model):
  """
  Student class
  """
  student_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20)
  enrollment_date = models.DateField()
  major = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes