from abc import abstractmethod
from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


# Task 4
def validate_specialities(specialty):
    validation_error_message = 'Specialty must be a valid choice.'
    specialities = ('Mammals', 'Birds', 'Reptiles', 'Others')
    if specialty not in specialities:
        raise ValidationError(validation_error_message)
    return specialty


# Task 1
class Animal(models.Model):
    NAME_MAX_LEN = 100
    SPECIES_MAX_LEN = 100
    SOUND_MAX_LEN = 100

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    species = models.CharField(
        max_length=SPECIES_MAX_LEN
    )
    birth_date = models.DateField()
    sound = models.CharField(
        max_length=SOUND_MAX_LEN
    )

    # Task 6
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age


class Mammal(Animal):
    FUR_COLOR_MAX_LEN = 50

    fur_color = models.CharField(
        max_length=FUR_COLOR_MAX_LEN
    )


class Bird(Animal):
    WING_SPAN_DECIMAL_PLACES = 2
    WING_SPAN_MAX_DIGITS = 5

    wing_span = models.DecimalField(
        max_digits=WING_SPAN_MAX_DIGITS,
        decimal_places=WING_SPAN_DECIMAL_PLACES
    )


class Reptile(Animal):
    SCALE_TYPE_MAX_LEN = 50

    scale_type = models.CharField(
        max_length=SCALE_TYPE_MAX_LEN
    )


# Task 2
class Employee(models.Model):
    FIRST_NAME_MAX_LEN = 50
    LAST_NAME_MAX_LEN = 50
    PHONE_NUM_MAX_LEN = 50

    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )
    phone_number = models.CharField(
        max_length=PHONE_NUM_MAX_LEN
    )

    @abstractmethod
    def __str__(self):
        ...


class SpecialityChoices(models.TextChoices):
    MAMMALS = 'Mammals', 'Mammals'
    BIRDS = 'Birds', 'Birds'
    REPTILES = 'Reptiles', 'Reptiles'
    OTHERS = 'Others', 'Others'


class ZooKeeper(Employee):
    SPECIALITY_MAX_LEN = 10

    specialty = models.CharField(
        max_length=SPECIALITY_MAX_LEN,
        choices=SpecialityChoices.choices,
        validators=(
            validate_specialities,
        )
    )
    managed_animals = models.ManyToManyField(
        Animal
    )

    def clean(self):
        if self.specialty not in ('Mammals', 'Birds', 'Reptiles', 'Others'):
            raise ValidationError("Specialty must be a valid choice.")

    def __str__(self):
        return self.__class__.__name__


# Task 7
class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ((True, 'Available'), (False, 'Not Available'))
        kwargs['default'] = True
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    LICENSE_NUMBER_MAX_LEN = 10

    license_number = models.CharField(
        max_length=LICENSE_NUMBER_MAX_LEN
    )
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability

    def __str__(self):
        return self.__class__.__name__


# Task 3
class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    # Task 5
    def display_info(self):
        extra_info = ''
        animal_info = (f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}. "
                       f"It makes a noise like '{self.sound}'!")

        if hasattr(self, 'mammal'):
            extra_info = f"Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, 'bird'):
            extra_info = f"Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, 'reptile'):
            extra_info = f"Its scale type is {self.reptile.scale_type}."

        if extra_info:
            return f'{animal_info} {extra_info}'
        return animal_info

    def is_endangered(self):
        endangered_spices = ("Cross River Gorilla", "Orangutan", "Green Turtle")
        return True if self.species in endangered_spices else False
