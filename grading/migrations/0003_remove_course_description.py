# Generated by Django 5.1.4 on 2024-12-16 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0002_alter_instructor_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]