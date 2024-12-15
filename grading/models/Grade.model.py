# from django.db import models
# from Student.model import Student
# from Course.model import Course

# class Grade(models.Model):
#   grade_id = models.AutoField(primary_key=True)
#   student = models.ForeignKey(Student, on_delete=models.CASCADE)
#   course = models.ForeignKey(Course, on_delete=models.CASCADE)
#   grade = models.DecimalField(max_digits=3, decimal_places=2)
#   semester = models.CharField(max_length=20)
#   academic_year = models.CharField(max_length=20)

#   class Meta:
#     unique_together = ('student', 'course', 'semester', 'academic_year')