from django.db import models
from django.utils import timezone


class Employee(models.Model):
    NAME_MAX_LEN = 30
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class LocationChoices(models.TextChoices):
    SOFIA = 'Sofia', 'Sofia'
    PLOVDIV = 'Plovdiv', 'Plovdiv'
    BURGAS = 'Burgas', 'Burgas'
    VARNA = 'Varna', 'Varna'


class Department(models.Model):
    CODE_MAX_LEN = 4
    NAME_MAX_LEN = 50
    DEFAULT_EMPLOYEES_COUNT = 1
    LOCATION_MAX_LEN = 20

    code = models.CharField(
        max_length=CODE_MAX_LEN,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True
    )
    employees_count = models.PositiveIntegerField(
        default=DEFAULT_EMPLOYEES_COUNT,
        verbose_name='Employees Count'
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
        null=True,
        blank=True,
        choices=LocationChoices.choices
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class Project(models.Model):
    PROJECT_NAME_MAX_LEN = 100
    BUDGET_MAX_DIGITS = 10
    BUDGET_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=PROJECT_NAME_MAX_LEN,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    budget = models.DecimalField(
        max_digits=BUDGET_MAX_DIGITS,
        decimal_places=BUDGET_DECIMAL_PLACES,
        null=True,
        blank=True
    )
    duration_in_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Duration in Days'
    )
    estimated_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Estimated Hours'
    )
    start_date = models.DateField(
        default=timezone.localdate,
        null=True,
        blank=True,
        verbose_name='Start Date'
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )
