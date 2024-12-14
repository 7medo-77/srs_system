class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255)
  course_code = models.CharField(max_length=20, unique=True)
  description = models.TextField()
  credits = models.IntegerField()
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