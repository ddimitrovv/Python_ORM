from django.db import models


class Pet(models.Model):
    NAME_MAX_LEN = 40
    SPECIES_MAX_LEN = 40

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    species = models.CharField(
        max_length=SPECIES_MAX_LEN
    )


class Artifact(models.Model):
    NAME_MAX_LEN = 70
    ORIGIN_MAX_LEN = 70
    DEFAULT_IS_MAGICAL = 'False'

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    origin = models.CharField(
        max_length=ORIGIN_MAX_LEN
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    is_magical = models.BooleanField(
        default=DEFAULT_IS_MAGICAL
    )


class Location(models.Model):
    NAME_MAX_LEN = 100
    REGION_MAX_LEN = 50
    DEFAULT_IS_CAPITAL = 'False'

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    region = models.CharField(
        max_length=REGION_MAX_LEN
    )
    population = models.PositiveIntegerField()
    description = models.TextField()
    is_capital = models.BooleanField(
        default=DEFAULT_IS_CAPITAL
    )


class Car(models.Model):
    MODEL_MAX_LEN = 40
    COLOR_MAX_LEN = 40
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2
    PRICE_WITH_DISCOUNT_MAX_DIGITS = 10
    PRICE_WITH_DISCOUNT_DECIMAL_PLACES = 2
    DEFAULT_PRICE_WITH_DISCOUNT = 0

    model = models.CharField(
        max_length=MODEL_MAX_LEN
    )
    year = models.PositiveIntegerField()
    color = models.CharField(
       max_length=COLOR_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    price_with_discount = models.DecimalField(
        max_digits=PRICE_WITH_DISCOUNT_MAX_DIGITS,
        decimal_places=PRICE_WITH_DISCOUNT_DECIMAL_PLACES,
        default=DEFAULT_PRICE_WITH_DISCOUNT
    )


class Task(models.Model):
    TITLE_MAX_LEN = 25
    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    description = models.TextField()
    due_date = models.DateField()
    is_finished = models.BooleanField(
        default=False
    )
