from faker import Faker
from grading.models.student import Student
from grading.models.department import Department
from grading.models.course import Course
from grading.models.instructor import Instructor
from grading.models.studentCourseEnrollment import StudentCourseEnrollment
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
# departments = []
# for key in fake_department.keys():
#     department = Department(
#         name=key, head_of_department=fake.name()
#     )
#     departments.append(department)

# print(departments)
# for dept in departments:
#   print(dept.department_id, dept.name, dept.head_of_department)

# Department.objects.bulk_create(departments)  # Bulk create departments
# print(Department.objects.all().first().__repr__())

departments = Department.objects.all()

# # Generate Instructors
# instructors = []
# for department in departments:
#     instructor_count = random_within_range(8, 15)
#     for _ in range(instructor_count):
#         instructor = Instructor(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             email=fake.email(),
#             phone_number=fake.lexify(text=('01?-????-????'), letters="0123456789"),
#             department=department,
#         )
#         instructors.append(instructor)
# # print( instructors )
# for instructor in instructors:
#   print(instructor.instructor_id, instructor.first_name, instructor.last_name, instructor.email, instructor.department, instructor.phone_number)
#   print('-'*30)
# Instructor.objects.bulk_create(instructors)  # Bulk create instructors

# Generate Courses (considering department and instructor relationships)
courseArray = []

for dep, courses in fake_department.items():
# for dep in departments:
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

# Course.objects.bulk_create(courseArray)  # Bulk create courses with assigned instructors

instructors = Instructor.objects.all()

# length = len(instructors)
# instructors_per_dept = len(instructors) - (length % len(departments)) / len(departments)
# dept_instructor_dict = {
#     departmentObject.name: {} for departmentObject in Department.objects.all()
# }

for index, inst in enumerate(instructors):
    # courses = list(inst.department.course_set.all())
    # inst.course_set.set(random.sample(courses, k=random.randint(1, 3)))
    print([course.course_name for course in inst.course_set.all() ])


# print(courseArray)

# # Generate Students
# students = []
# for _ in range(100):
#     student = Student(
#         first_name=fake.first_name(),
#         last_name=fake.last_name(),
#         email=fake.email(),
#         phone_number=fake.phone_number(),
#         enrollment_date=fake.date(),
#         major=fake.job(),
#         date_of_birth=fake.date(past=30 * 365),  # Generate DOBs within past 30 years
#         department=departments[random_within_range(0, len(departments) - 1)],  # Random department
#     )
#     students.append(student)
# print(students)
# # Student.objects.bulk_create(students)  # Bulk create students

# # Generate Student Course Enrollments (considering student enrollment range)
# enrollments = []
# for student in students:
#     course_choices = courses.copy()  # Copy the list to avoid duplicates
#     enrollment_count = random_within_range(5, 7)
#     for _ in range(enrollment_count):
#         chosen_course = course_choices.pop(randint(0, len(course_choices) - 1))
#         enrollment = StudentCourseEnrollment(
#             student=student,
#             course=chosen_course,
#             instructor=chosen_course.instructors.first(),  # Pick one random instructor
#             date=fake.date(),
#             semester=fake.random.choice(["Fall", "Spring", "Summer"]),
#             academic_year=random_within_range(2022, 2024),
#             grade=round(fake.random.uniform(60, 100), 2),  # Random grades between 60 and 100 (rounded to 2 decimal places)
#         )
#         enrollments.append(enrollment)
# print(enrollments)
# # StudentCourseEnrollment.objects.bulk_create(enrollments)  # Bulk create student enrollments

print(f"Generated {len(departments)} Departments")
print(f"Generated {len(instructors)} Instructors")
# # print(f"Generated {len(courses)} Courses")
# # print(f"Generated {len(students)} Students")
# # # print(