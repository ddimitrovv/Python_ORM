from django.db import models


# Task 1
class Pet(models.Model):
    NAME_MAX_LEN = 40
    SPECIES_MAX_LEN = 40

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    species = models.CharField(
        max_length=SPECIES_MAX_LEN
    )


# Task 2
class Artifact(models.Model):
    NAME_MAX_LEN = 70
    ORIGIN_MAX_LEN = 70
    DEFAULT_IS_MAGICAL = False

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


# Task 3
class Location(models.Model):
    NAME_MAX_LEN = 100
    REGION_MAX_LEN = 50
    DEFAULT_IS_CAPITAL = False

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


# Task 4
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


# Task 5
class Task(models.Model):
    TITLE_MAX_LEN = 25
    DEFAULT_IS_FINISHED = False
    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    description = models.TextField()
    due_date = models.DateField()
    is_finished = models.BooleanField(
        default=DEFAULT_IS_FINISHED
    )


# Task 6
class RoomChoices(models.TextChoices):
    STANDARD = 'Standard', 'Standard'
    DELUXE = 'Deluxe', 'Deluxe'
    SUITE = 'Suite', 'Suite'


class HotelRoom(models.Model):
    ROOM_TYPE_MAX_LEN = 20
    PRICE_PER_NIGHT_MAX_DIGITS = 8
    PRICE_PER_NIGHT_DECIMAL_PLACES = 2
    DEFAULT_IS_RESERVED = False

    room_number = models.PositiveIntegerField()
    room_type = models.CharField(
        max_length=ROOM_TYPE_MAX_LEN,
        choices=RoomChoices.choices
    )
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    price_per_night = models.DecimalField(
        max_digits=PRICE_PER_NIGHT_MAX_DIGITS,
        decimal_places=PRICE_PER_NIGHT_DECIMAL_PLACES
    )
    is_reserved = models.BooleanField(
        default=DEFAULT_IS_RESERVED
    )


# Task 7
class CharacterChoices(models.TextChoices):
    MAGE = 'Mage', 'Mage'
    WARRIOR = 'Warrior', 'Warrior'
    ASSASSIN = 'Assassin', 'Assassin'
    SCOUT = 'Scout', 'Scout'
    FUSION = 'Fusion', 'Fusion'


class Character(models.Model):
    NAME_MAX_LEN = 100
    CLASS_NAME_MAX_LEN = 10
    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    class_name = models.CharField(
        max_length=CLASS_NAME_MAX_LEN,
        choices=CharacterChoices.choices
    )
    level = models.PositiveIntegerField()
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    hit_points = models.PositiveIntegerField()
    inventory = models.TextField()
