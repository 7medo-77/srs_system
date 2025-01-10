from django.db import models
from grading.models.department import Department
from grading.models.instructor import Instructor
from grading.models.student import Student

class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255, unique=True)
  course_code = models.CharField(max_length=20, unique=True)
  # description = models.TextField()
  credits = models.IntegerField()

  studentEnrollment = models.ManyToManyField(Student, through="StudentCourseEnrollment")
  department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")
  instructors = models.ManyToManyField(Instructor, related_name="courses")

  def __str__(self):
      return self.course_name

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

  class Meta:
    db_table="courses"