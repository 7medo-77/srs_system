# Generated by Django 5.1.4 on 2024-12-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]