from django.core.validators import MaxLengthValidator
from django.db import models


class Person(models.Model):
    NAME_MAX_LEN = 30
    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    age = models.PositiveIntegerField()


class Blog(models.Model):
    AUTHOR_MAX_LEN = 35
    post = models.TextField()
    author = models.CharField(
        max_length=AUTHOR_MAX_LEN
    )


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()


class Recipe(models.Model):
    NAME_MAX_LEN = 100
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True
    )
    description = models.TextField()
    ingredients = models.TextField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Product(models.Model):
    NAME_MAX_LEN = 70
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class UserProfile(models.Model):
    USERNAME_MAX_LEN = 65
    FIRST_NAME_MAX_LEN = 40
    LAST_NAME_MAX_LEN = 40
    BIO_MAX_LEN = 120

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        unique=True
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        unique=True
    )
    bio = models.TextField(
        max_length=BIO_MAX_LEN
    )
    email = models.EmailField(
        default="students@softuni.bg",
        unique=True
    )
    profile_image_url = models.URLField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Exercise(models.Model):
    NAME_MAX_LEN = 100
    DIFFICULTY_LEVEL_MAX_LEN = 20
    EQUIPMENT_MAX_LEN = 90
    DEFAULT_CALORIES_BURNED = 0

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=DIFFICULTY_LEVEL_MAX_LEN,
        verbose_name='Difficulty Level'
    )
    duration_minutes = models.PositiveIntegerField(
        verbose_name='Duration Minutes'
    )
    equipment = models.CharField(
        max_length=EQUIPMENT_MAX_LEN
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Video URL'
    )
    calories_burned = models.PositiveIntegerField(
        default=DEFAULT_CALORIES_BURNED,
        verbose_name='Calories Burned'
    )
    is_favorite = models.BooleanField(
        default=False,
        verbose_name='Is Favourite'
    )


class GenreChoices(models.TextChoices):
    FICTION = "Fiction", "Fiction"
    NON_FICTION = "Non-Fiction", "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction", "Science Fiction"
    HORROR = "Horror", "Horror"


class Book(models.Model):
    TITLE_MAX_LEN = 30
    AUTHOR_MAX_LEN = 100
    GENRE_MAX_LEN = 20
    PRICE_MAX_DIGITS = 8
    PRICE_DECIMAL_PLACES = 2

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    author = models.CharField(
        max_length=AUTHOR_MAX_LEN
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GenreChoices.choices
    )
    publication_date = models.DateField(
        editable=False,
        auto_now_add=True,
        verbose_name="Publication Date"
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Is Available"
    )
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title
