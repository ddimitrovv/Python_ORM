from _decimal import Decimal
from django.contrib.postgres.search import SearchVectorField

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator, URLValidator, MinLengthValidator
from django.db import models


# Task 1
def validate_age(value):
    if value < 18:
        raise ValidationError("Age must be greater than 18")


class Customer(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]*$',
        message="Name can only contain letters and spaces",
    )

    email_validator = EmailValidator(
        message="Enter a valid email address",
    )

    phone_number_validator = RegexValidator(
        regex=r'^\+359\d{9}$',
        message="Phone number must start with '+359' followed by 9 digits",
    )

    website_url_validator = URLValidator(
        message="Enter a valid URL",
    )

    name = models.CharField(
        max_length=100,
        validators=[name_validator]
    )

    age = models.PositiveIntegerField(
        validators=(
            validate_age,
        )
    )

    email = models.EmailField(
        error_messages={
            "invalid": "Enter a valid email address"
        }
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[phone_number_validator]
    )

    website_url = models.URLField(
        error_messages={
            "invalid": "Enter a valid URL"
        }
    )


# Task 2
class BaseMedia(models.Model):
    TITLE_MAX_LEN = 100
    GENRE_MAX_LEN = 50

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    description = models.TextField()
    genre = models.CharField(
        max_length=GENRE_MAX_LEN
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Book(BaseMedia):
    AUTHOR_MAX_LEN = 100
    AUTHOR_MIN_LEN = 5
    ISBN_MAX_LEN = 20
    ISBN_MIN_LEN = 6

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

    author = models.CharField(
        max_length=AUTHOR_MAX_LEN,
        validators=(
            MinLengthValidator(AUTHOR_MIN_LEN, "Author must be at least 5 characters long"),
        ),
    )
    isbn = models.CharField(
        max_length=ISBN_MAX_LEN,
        validators=(
            MinLengthValidator(ISBN_MIN_LEN, "ISBN must be at least 6 characters long"),
        ),
    )


class Movie(BaseMedia):
    DIRECTOR_MAX_LEN = 100
    DIRECTOR_MIN_LEN = 8

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

    director = models.CharField(
        max_length=DIRECTOR_MAX_LEN,
        validators=(
            MinLengthValidator(DIRECTOR_MIN_LEN, "Director must be at least 8 characters long"),
        ),
    )


class Music(BaseMedia):
    DIRECTOR_MAX_LEN = 100
    DIRECTOR_MIN_LEN = 9

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'

    artist = models.CharField(
        max_length=DIRECTOR_MAX_LEN,
        validators=(
            MinLengthValidator(DIRECTOR_MIN_LEN, "Artist must be at least 9 characters long"),
        ),
    )


# Task 3
class Product(models.Model):
    NAME_MAX_LEN = 100
    PRICE_DECIMAL_PLACES = 2
    PRICE_MAX_DIGITS = 10

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )

    def calculate_tax(self):
        return (self.price * 8) / 100

    @staticmethod
    def calculate_shipping_cost(weight):
        return weight * Decimal(2.00)

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return self.price * Decimal(1.20)

    def calculate_tax(self):
        return (self.price * 5) / 100

    @staticmethod
    def calculate_shipping_cost(weight: Decimal):
        return weight * Decimal(1.50)

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


# Task 4
class RechargeEnergyMixin:

    def recharge_energy(self, amount):
        self.energy = self.energy + amount if self.energy + amount < 100 else 100
        if self.energy < 0:
            self.energy = 0

        return self.energy


class Hero(models.Model, RechargeEnergyMixin):
    NAME_MAX_LEN = 100
    HERO_TITLE_MAX_LEN = 100

    name = models.CharField(max_length=NAME_MAX_LEN)
    hero_title = models.CharField(max_length=HERO_TITLE_MAX_LEN)
    energy = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class SpiderHero(Hero):

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy >= 80:
            self.energy = self.recharge_energy(-80)
            return f"{self.name} as Spider Hero swings from buildings using web shooters"
        return f"{self.name} as Spider Hero is out of web shooter fluid"


class FlashHero(Hero):

    class Meta:
        proxy = True

    def run_at_super_speed(self):
        if self.energy >= 65:
            self.energy = self.recharge_energy(-65)
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"
        return f"{self.name} as Flash Hero needs to recharge the speed force"


# Task 5
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [models.Index(fields=['search_vector'])]
