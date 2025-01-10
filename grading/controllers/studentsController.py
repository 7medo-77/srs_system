from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from grading.models.student import Student
from grading.models.studentCourseEnrollment import StudentCourseEnrollment
from grading.models.instructor import Instructor
from authentication.models.AuthUser import AuthUser
import csv
import pickle

# Decorator to ensure only logged-in users can access these views
@login_required
def getAllStudents(request):
    """
    Retrieve all students, paginate the results, and use a recursive function to fetch all students.
    """
    # Get all students
    students_list = Student.objects.all()

    # Paginate the results (10 students per page)
    paginator = Paginator(students_list, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    # Recursive function to fetch all students
    def fetch_all_students(students, all_students=None):
        if all_students is None:
            all_students = []
        for student in students:
            all_students.append(student)
        return all_students

    all_students = fetch_all_students(students)

    return render(request, 'grading/students/list.html', {'students': students, 'all_students': all_students})

@login_required
def getStudentDetails(request, user_id):
    """
    Retrieve all courses the student is enrolled in, calculate GPA, and pass it to the template.
    """
    # Get the student object or return 404 if not found
    user = get_object_or_404(AuthUser, id=user_id)
    student = user.student_profile

    # Get all enrollments for the student
    enrollments = StudentCourseEnrollment.objects.filter(student=student)

    # Calculate GPA
    total_grade_points = 0
    total_credits = 0
    for enrollment in enrollments:
        total_grade_points += enrollment.grade * enrollment.course.credits
        total_credits += enrollment.course.credits
    gpa = ((total_grade_points / total_credits) / 100) * 4 if total_credits > 0 else 0

    return render(request, 'grading/students/details.html', {
        'student': student,
        'enrollments': enrollments,
        'gpa': round(gpa, 2),
    })

@login_required
def getStudentInstructors(request, user_id):
    """
    Retrieve all instructors associated with the student's courses.
    """
    # Get the student object or return 404 if not found
    user = get_object_or_404(AuthUser, id=user_id)
    student = user.student_profile
    instructors = student.enrollments

    # Get all enrollments for the student
    enrollments = StudentCourseEnrollment.objects.filter(student=student)
    print(enrollments)

    # Get unique instructors from the enrollments
    instructors = [enrollment.instructor for enrollment in enrollments]

    # for enrollment in enrollments:
    #     print(enrollment.instructor.user.first_name)
    #     instructors.add()

    return render(request, 'grading/students/studentInstructors.html', {
        'student': student,
        'instructors': instructors,
        'enrollments': enrollments,
    })

@login_required
def exportStudentsToCSV(request):
    """
    Export all students to a CSV file.
    """
    students = Student.objects.all()

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student ID', 'Name', 'Major', 'Date of Birth'])

    for student in students:
        writer.writerow([
            student.user_id,
            f"{student.user.first_name} {student.user.last_name}",
            student.major.name,
            student.date_of_birth,
        ])

    return response

@login_required
def saveStudentsToBinary(request):
    """
    Save all students to a binary file using pickle.
    """
    students = Student.objects.all()
    data = []

    for student in students:
        data.append({
            'student_id': student.student_id,
            'name': f"{student.user.first_name} {student.user.last_name}",
            'major': student.major.name,
            'date_of_birth': student.date_of_birth,
        })

    # Save data to a binary file
    with open('students_data.bin', 'wb') as file:
        pickle.dump(data, file)

    return HttpResponse("Student data saved to binary file.")