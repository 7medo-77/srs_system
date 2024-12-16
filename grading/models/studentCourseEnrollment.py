from django.db import models
from django.db.models import UniqueConstraint
from grading.models.student import Student
from grading.models.course import Course
from grading.models.instructor import Instructor

class StudentCourseEnrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  date = models.DateField()
  semester = models.CharField(max_length=255)
  academic_year = models.IntegerField()
  grade = models.DecimalField(max_digits=3, decimal_places=2)

  def __repr__(self):
    attributes = ",".join([str(value) for value in vars(self).values()][1:])
    return attributes

  class Meta:
    unique_together = ('student', 'course')
    constraints: [
      UniqueConstraint(
        fields=[ 'student', 'course' ],
        name="uniqueEnrollment"
      )
    ]