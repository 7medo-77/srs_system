from faker import Faker
from random import randint
from grading.models.student import Student
from grading.models.department import Department
from grading.models.course import Course
from grading.models.instructor import Instructor
from grading.models.studentCourseEnrollment import StudentCourseEnrollment

# Initialize Faker
fake = Faker()

# Define function to generate random number within a range (inclusive)
def random_within_range(low, high):
    return randint(low, high)

# Generate Departments
departments = []
for _ in range(5):
    department = Department(
        name=fake.company(), head_of_department=fake.name()
    )
    departments.append(department)
# print(departments)
# for dept in departments:
  # print(dept.department_id, dept.name, dept.head_of_department)

Department.objects.bulk_create(departments)  # Bulk create departments

# Generate Instructors
instructors = []
for department in departments:
    instructor_count = random_within_range(4, 6)
    for _ in range(instructor_count):
        instructor = Instructor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            department=department,
        )
        instructors.append(instructor)
print( instructors )
# Instructor.objects.bulk_create(instructors)  # Bulk create instructors

# Generate Courses (considering department and instructor relationships)
courses = []
for department in departments:
    course_count = random_within_range(3, 7)
    for _ in range(course_count):
        course = Course(
            course_name=fake.job(),
            course_code=fake.unique.lexify(text="CS###"),
            description=fake.text(),
            credits=random_within_range(3, 4),
            department=department,
        )
        # Assign random instructors to the course (avoid duplicates)
        instructor_choices = instructors.copy()
        instructor_count = random_within_range(1, len(instructor_choices))
        assigned_instructors = []
        for _ in range(instructor_count):
            chosen_instructor = instructor_choices.pop(randint(0, len(instructor_choices) - 1))
            assigned_instructors.append(chosen_instructor)
        course.instructors.add(*assigned_instructors)
        courses.append(course)
print(courses)
# Course.objects.bulk_create(courses)  # Bulk create courses with assigned instructors

# Generate Students
students = []
for _ in range(100):
    student = Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        enrollment_date=fake.date(),
        major=fake.job(),
        date_of_birth=fake.date(past=30 * 365),  # Generate DOBs within past 30 years
        department=departments[random_within_range(0, len(departments) - 1)],  # Random department
    )
    students.append(student)
print(students)
# Student.objects.bulk_create(students)  # Bulk create students

# Generate Student Course Enrollments (considering student enrollment range)
enrollments = []
for student in students:
    course_choices = courses.copy()  # Copy the list to avoid duplicates
    enrollment_count = random_within_range(5, 7)
    for _ in range(enrollment_count):
        chosen_course = course_choices.pop(randint(0, len(course_choices) - 1))
        enrollment = StudentCourseEnrollment(
            student=student,
            course=chosen_course,
            instructor=chosen_course.instructors.first(),  # Pick one random instructor
            date=fake.date(),
            semester=fake.random.choice(["Fall", "Spring", "Summer"]),
            academic_year=random_within_range(2022, 2024),
            grade=round(fake.random.uniform(60, 100), 2),  # Random grades between 60 and 100 (rounded to 2 decimal places)
        )
        enrollments.append(enrollment)
print(enrollments)
# StudentCourseEnrollment.objects.bulk_create(enrollments)  # Bulk create student enrollments

print(f"Generated {len(departments)} Departments")
print(f"Generated {len(instructors)} Instructors")
print(f"Generated {len(courses)} Courses")
print(f"Generated {len(students)} Students")
# print(