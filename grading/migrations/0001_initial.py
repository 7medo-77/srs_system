# Generated by Django 5.1.4 on 2024-12-15 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('head_of_department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grading.department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('credits', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grading.department')),
                ('instructors', models.ManyToManyField(to='grading.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('semester', models.CharField(max_length=255)),
                ('academic_year', models.IntegerField()),
                ('grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grading.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grading.instructor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grading.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='studentEnrollment',
            field=models.ManyToManyField(through='grading.StudentCourseEnrollment', to='grading.student'),
        ),
    ]
