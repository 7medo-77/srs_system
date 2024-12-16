from django.db import models
from grading.models.department import Department
from grading.models.instructor import Instructor
from grading.models.student import Student

class Department(models.Model):
  department_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  head_of_department = models.CharField(max_length=255)

  def __str__(self):
    return self.name

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

class Instructor(models.Model):
  instructor_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

class Student(models.Model):
  """
  Student class
  """
  student_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20)
  major = models.CharField(max_length=255)
  date_of_birth = models.DateField()

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255)
  course_code = models.CharField(max_length=20, unique=True)
  description = models.TextField()
  credits = models.IntegerField()
  studentEnrollment = models.ManyToManyField(Student, through="StudentCourseEnrollment")
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  instructors = models.ManyToManyField(Instructor)

  def __str__(self):
      return self.course_name

  def __repr__(self):
    """
    String representation for CSV parsing
    """
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

class StudentCourseEnrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  date = models.DateField()
  semester = models.CharField(max_length=255)
  academic_year = models.IntegerField()
  grade = models.DecimalField(max_digits=3, decimal_places=2)

  def __repr__(self):
    attributes = ",".join([str(value) for value in vars(self).values()])
    return attributes

  class Meta:
    unique_together = ('student', 'course')
    constraints: [
      UniqueConstraint(
        fields=[ 'student', 'course' ],
        name="uniqueEnrollment"
      )
    ]