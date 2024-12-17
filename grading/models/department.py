from django.db import models

class Department(models.Model):
  department_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, unique=True)
  head_of_department = models.CharField(max_length=255)

  def __str__(self):
    return self.name

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()][1:])
    return attributes