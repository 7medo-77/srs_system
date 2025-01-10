"""
URL configuration for grading app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from grading.controllers.studentsController import *

app_name = 'grading'
urlpatterns = [
    # path('', getAllStudents, name='all-students' ),
    path('students/', getAllStudents, name='all-students'),
    path('students/<int:user_id>/', getStudentDetails, name='student-details'),
    path('students/<int:user_id>/instructors/', getStudentInstructors, name='student-instructors'),
    path('students/export-csv/', exportStudentsToCSV, name='export-students-csv'),
    path('students/save-binary/', saveStudentsToBinary, name='save-students-binary'),
]