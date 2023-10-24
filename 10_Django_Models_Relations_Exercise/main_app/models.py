from django.db import models


# Task 1
class Author(models.Model):
    NAME_MAX_LEN = 40

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )


class Book(models.Model):
    TITLE_MAX_LEN = 40
    PRICE_MAX_DIGITS = 5
    PRICE_DECIMAL_PLACES = 2

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )


# Task 2
class Song(models.Model):
    TITLE_MAX_LEN = 100

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True
    )


class Artist(models.Model):
    NAME_MAX_LEN = 100

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    songs = models.ManyToManyField(
        Song,
        related_name='artists'
    )


# Task 3
class Product(models.Model):
    NAME_MAX_LEN = 100

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True
    )


class Review(models.Model):
    DESCRIPTION_MAX_LEN = 200

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN
    )
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='reviews'
    )


# Task 4
class Driver(models.Model):
    FIRST_NAME_MAX_LEN = 50
    LAST_NAME_MAX_LEN = 50

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )


class DrivingLicense(models.Model):
    LICENSE_NUMBER_MAX_LEN = 10

    license_number = models.TextField(
        max_length=LICENSE_NUMBER_MAX_LEN,
        unique=True
    )
    issue_date = models.DateField()
    driver = models.OneToOneField(
        Driver,
        on_delete=models.CASCADE
    )


# Task 5
class Owner(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )


class Car(models.Model):
    MODEL_MAX_LEN = 50

    model = models.CharField(
        max_length=MODEL_MAX_LEN
    )
    year = models.PositiveIntegerField()
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cars'
    )


class Registration(models.Model):
    REGISTRATION_NUMBER_MAX_LEN = 10

    registration_number = models.CharField(
        max_length=REGISTRATION_NUMBER_MAX_LEN,
        unique=True
    )
    registration_date = models.DateField(
        blank=True,
        null=True
    )
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='registration'
    )

