import os
import django
from datetime import date

from main_app.models import Student

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def add_students():
    students_data = [
        {
            "student_id": "FC5204",
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "1995-05-15",
            "email": "john.doe@university.com",
        },
        {
            "student_id": "FE0054",
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@university.com",
        },
        {
            "student_id": "FH2014",
            "first_name": "Alice",
            "last_name": "Johnson",
            "birth_date": "1998-02-10",
            "email": "alice.johnson@university.com",
        },
        {
            "student_id": "FH2015",
            "first_name": "Bob",
            "last_name": "Wilson",
            "birth_date": "1996-11-25",
            "email": "bob.wilson@university.com",
        },
    ]

    for student_data in students_data:
        student, created = Student.objects.get_or_create(
            student_id=student_data["student_id"],
            defaults=student_data
        )


# add_students()
# print(Student.objects.all())


def get_students_info():
    all_students = Student.objects.all()
    output = []
    for student in all_students:
        output.append(f'Student №{student.pk}: {student.first_name} {student.last_name}; Email: {student.email}')

    return '\n'.join(output)


# print(get_students_info())


def update_students_emails():
    all_students = Student.objects.all()
    for student in all_students:
        student.email = student.email.replace('university.com', 'uni-students.com')
        student.save()


# print(update_students_emails())


def truncate_students():
    Student.objects.all().delete()
