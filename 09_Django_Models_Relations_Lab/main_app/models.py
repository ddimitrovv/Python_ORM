from django.db import models
from django.utils import timezone


# Task 1
class Lecturer(models.Model):
    FIRST_NAME_MAX_LEN = 100
    LAST_NAME_MAX_LEN = 100

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    NAME_MAX_LEN = 100
    CODE_MAX_LEN = 10

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    code = models.CharField(
        max_length=CODE_MAX_LEN
    )
    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# Task 2
class Student(models.Model):
    STUDENT_ID_MAX_LEN = 10
    FIRST_NAME_MAX_LEN = 100
    LAST_NAME_MAX_LEN = 100

    student_id = models.CharField(
        primary_key=True,
        max_length=10
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )
    birth_date = models.DateField()
    email = models.EmailField(
        unique=True
    )
    subjects = models.ManyToManyField(
        to=Subject,
        through='StudentEnrollment',
    )


# # Task 3
class GradeChoices(models.TextChoices):
    A = 'A', 'A'
    B = 'B', 'B'
    C = 'C', 'C'
    D = 'D', 'D'
    F = 'F', 'F'


class StudentEnrollment(models.Model):
    GRADE_MAX_LEN = 1

    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE
    )
    enrollment_date = models.DateField(
        default=timezone.now()
    )

    grade = models.CharField(
        max_length=GRADE_MAX_LEN,
        choices=GradeChoices.choices,
    )


# Task 4
class LecturerProfile(models.Model):
    OFFICE_LOCATION_MAX_LEN = 100

    lecturer = models.OneToOneField(
        Lecturer,
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        unique=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    office_location = models.CharField(
        max_length=OFFICE_LOCATION_MAX_LEN,
        blank=True,
        null=True
    )
