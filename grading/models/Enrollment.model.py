class Enrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  class Meta:
      unique_together = ('student', 'course')