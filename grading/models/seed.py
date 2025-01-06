from faker import Faker
from grading.models.student import Student
from grading.models.department import Department
from grading.models.course import Course
from grading.models.instructor import Instructor
from grading.models.studentCourseEnrollment import StudentCourseEnrollment
from authentication.models.AuthUser import AuthUser

import datetime
import random

# Initialize Faker
fake = Faker()

# Define function to generate random number within a range (inclusive)
def random_within_range(low, high):
    return random.randint(low, high)

fake_department = {
    "Computer Science": [
        "Data Structures and Algorithms",
        "Operating Systems",
        "Artificial Intelligence",
        "Database Management Systems",
        "Web Development and Technologies",

    ],
    "Mechanical Engineering": [
        "Thermodynamics and Fluid Dynamics",
        "Fluid Mechanics",
        "Materials Science and Engineering",
        "Computer-Aided Design",
        "Robotics and Automation",

    ],
    "English Literature": [
        "Shakespearean Drama",
        "Modernist Literature",
        "Introduction to Literary Theory",
        "Creative Writing and Poetry",
        "World Literature in Translation",

    ],
    "Business Administration": [
        "Principles of Marketing",
        "Financial Accounting",
        "Organizational Behavior",
        "Business Ethics and Corporate Governance",
        "Entrepreneurship and Innovation",

    ],
    "Psychology Department": [
        "Introduction to Psychology",
        "Cognitive Psychology",
        "Abnormal Psychology",
        "Social Psychology",
        "Research Methods in Psychology",

    ],
 }

# Generate Departments
departmentResult = Department.objects.all()
departments = []

if len(departmentResult) == 0:
    for key in fake_department.keys():
        department = Department(
            name=key, head_of_department=fake.name()
        )
        departments.append(department)
    Department.objects.bulk_create(departments)  # Bulk create departments

# print(departments)
# for dept in departments:
#   print(dept.department_id, dept.name, dept.head_of_department)

# print(Department.objects.all().first().__repr__())

departments = Department.objects.all()

instructorResult = Instructor.objects.all()
instructors = []
instructor_profiles = []
# Generate Instructors
if len(instructorResult) == 0:
    for department in departments:
        instructor_count = random_within_range(8, 15)
        for _ in range(instructor_count):
            first_name=fake.first_name()
            password=first_name
            instructor_profile = AuthUser(
                first_name=first_name,
                last_name=fake.last_name(),
                email=fake.email(),
                password=password,
                phone_number=fake.lexify(text=('01?-'), letters="0125") + fake.lexify(text=('????-????'), letters="0123456789"),
            )
            instructor_profiles.append(instructor_profile)

            instructor = Instructor(
                user=instructor_profile,
                department=department,
            )
            instructors.append(instructor)

    AuthUser.objects.bulk_create(instructor_profiles)  # Bulk create instructor_profiles
    Instructor.objects.bulk_create(instructors)  # Bulk create instructors

# # print( instructors )
# for instructor in instructors:
#   print(instructor.instructor_id, instructor.first_name, instructor.last_name, instructor.email, instructor.department, instructor.phone_number)
#   print('-'*30)


# Generate Courses (considering department and instructor relationships)
courseResult = Course.objects.all()
courseArray = []

if len(courseResult) == 0:
    for dep, courses in fake_department.items():
        for index, course in enumerate(courses):
            course_code_initials = ''.join([name[0] for name in course.split(' ') if name[0].isupper()])
            result_department = Department.objects.get(name=dep)

            courseObject = Course(
                course_name=fake_department[dep][index],
                # course_code=fake.unique.lexify(text="CS###"),
                course_code=fake.unique.lexify(text=f"{course_code_initials}???", letters="0123456789"),
                # description=fake.text(),
                credits=random_within_range(1, 5),
                department=result_department,
            )
            courseArray.append(courseObject)

    Course.objects.bulk_create(courseArray)  # Bulk create courses with assigned instructors

    instructors = Instructor.objects.all()

    for index, inst in enumerate(instructors):
        courses = list(inst.department.courses.all())
        inst.courses.set(random.sample(courses, k=random.randint(1, 3)))
        print([course.course_name for course in inst.courses.all() ])


# print(courseArray)

# Generate Students
studentResult = Student.objects.all()
students = []
enrollments = []
if len(studentResult) == 0:
    for department in Department.objects.all():
        courses = list(department.courses.all())

        for i in range(random.randint(150, 250)):
            student = Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                # phone_number=fake.phone_number(),
                phone_number=fake.lexify(text=('01?-????-????'), letters="0123456789"),
                # enrollment_date=fake.date_between(start_date=datetime.date(2019, 1, 1) , end_date=datetime.date(2024, 9, 1)),
                major=department,
                date_of_birth=fake.date_between(start_date=datetime.date(1997, 1, 1) , end_date=datetime.date(2007, 12, 30)),
            )
            for course in courses:
                float_num = random.uniform(0,1)
                probability = round(float_num)
                # print(course.instructor)

                if probability == 0:
                    continue

                instructors = list(course.instructors.all())
                fake_year = random_within_range(2020, 2024)
                fake_semester=fake.random.choice(["Fall", "Spring", "Summer"]),

                if fake_semester == "fall":
                    fake_date = fake.date_between(start_date=datetime.date(fake_year, 8, 1) , end_date=datetime.date(fake_year, 10, 15))
                elif fake_semester == "spring":
                    fake_date = fake.date_between(start_date=datetime.date(fake_year, 1, 1) , end_date=datetime.date(fake_year, 2, 20))
                else:
                    fake_date = fake.date_between(start_date=datetime.date(fake_year, 6, 1) , end_date=datetime.date(fake_year, 7, 15))

                fake_grade=round(random.uniform(60, 99), 2)
                # print(fake_grade)

                enrollment = StudentCourseEnrollment.objects.create(
                    student=student,
                    course=course,
                    instructor=random.choice(instructors),
                    date=fake_date,
                    semester=fake_semester,
                    academic_year=fake_year,
                    grade=fake_grade
                )
                enrollments.append(enrollments)
            students.append(student)
    Student.objects.bulk_create(students)  # Bulk create students

# print(students)
for stu in students:
    print(stu.__repr__())

# Generate Student Course Enrollments (considering student enrollment range)
enrollmentResult = StudentCourseEnrollment.objects.all()
enrollments = []
if len( enrollmentResult ) == 0:
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
    StudentCourseEnrollment.objects.bulk_create(enrollments)  # Bulk create student enrollments

print(f"Generated {len(departments)} Departments")
print(f"Generated {len(instructors)} Instructors")
print(f"Generated {len(courseArray)} Courses")
print(f"Generated {len(students)} Students")
print(f"Generated {len(enrollments)} Enrollments")