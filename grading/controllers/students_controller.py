from django.shortcuts import render
from django.http import HttpResponse
from grading.models.student import Student

def getAllStudents(request):
  allStudents = Student.objects.all()
  return render(request, 'grading/students/list.html', { 'allStudents': allStudents.values() })