from django.db import models
from django.utils import timezone


class Shoe(models.Model):
    BRAND_MAX_LEN = 25

    brand = models.CharField(
        max_length=BRAND_MAX_LEN
    )
    size = models.PositiveIntegerField()


class UniqueBrands(models.Model):
    BRAND_NAME_MAX_LEN = 25

    brand_name = models.CharField(
        max_length=BRAND_NAME_MAX_LEN,
        verbose_name='Brand Name'
    )


class EventRegistration(models.Model):
    EVENT_NAME_MAX_LEN = 60
    PARTICIPANT_NAME_MAX_LEN = 50

    event_name = models.CharField(
        max_length=EVENT_NAME_MAX_LEN
    )
    participant_name = models.CharField(
        max_length=PARTICIPANT_NAME_MAX_LEN
    )
    registration_date = models.DateField(
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        return f'{self.participant_name} - {self.event_name}'


class Movie(models.Model):
    TITLE_MAX_LEN = 100
    DIRECTOR_MAX_LEN = 100
    GENRE_MAX_LEN = 50

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    director = models.CharField(
        max_length=DIRECTOR_MAX_LEN
    )
    release_year = models.PositiveIntegerField()
    genre = models.CharField(
        max_length=GENRE_MAX_LEN
    )

    def __str__(self):
        return f'Movie "{self.title}" by {self.director}'


class Student(models.Model):
    FIRST_NAME_MAX_LEN = 50
    LAST_NAME_MAX_LEN = 50
    GRADE_MAX_LEN = 10
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN
    )
    age = models.PositiveIntegerField()
    grade = models.CharField(
        max_length=GRADE_MAX_LEN
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Supplier(models.Model):
    NAME_MAX_LEN = 100
    CONTACT_PERSON_MAX_LEN = 50
    PHONE_MAX_LEN = 20
    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    contact_person = models.CharField(
        max_length=CONTACT_PERSON_MAX_LEN
    )
    email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        max_length=PHONE_MAX_LEN,
        unique=True)

    address = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Course(models.Model):
    TITLE_MAX_LEN = 90
    LECTURER_MAX_LEN = 90
    DESCRIPTION_MAX_LEN = 200
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    lecturer = models.CharField(
        max_length=LECTURER_MAX_LEN
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    start_date = models.DateField(
        default=timezone.now
    )
    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.title} - {self.lecturer}"

    class Meta:
        ordering = ['-start_date']


class Person(models.Model):
    NAME_MAX_LEN = 40
    AGE_GROUP_MAX_LEN = 20

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    age = models.PositiveIntegerField()
    age_group = models.CharField(
        max_length=AGE_GROUP_MAX_LEN,
        default='No age group'
    )

    def __str__(self):
        return f'Name: {self.name}'


class Item(models.Model):
    NAME_MAX_LEN = 100
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2
    DEFAULT_QUANTITY = 0
    RARITY_MAX_LEN = 20
    DEFAULT_RARITY = 'empty'

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )
    quantity = models.PositiveIntegerField(
        default=DEFAULT_QUANTITY
    )
    rarity = models.CharField(
        max_length=RARITY_MAX_LEN,
        default=DEFAULT_RARITY
    )

    def __str__(self):
        return self.name


class Smartphone(models.Model):
    BRAND_MAX_LEN = 100
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2
    DEFAULT_PRICE = 0
    CATEGORY_MAX_LEN = 20
    DEFAULT_CATEGORY = 'empty'

    brand = models.CharField(
        max_length=BRAND_MAX_LEN
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        default=DEFAULT_PRICE
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        default=DEFAULT_CATEGORY
    )

    def __str__(self):
        return self.brand


class StatusChoices(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    COMPLETED = 'Completed', 'Completed'
    CANCELLED = 'Cancelled', 'Cancelled'


class Order(models.Model):
    PRODUCT_NAME_MAX_LEN = 30
    CUSTOMER_NAME_MAX_LEN = 100
    STATUS_MAX_LEN = 30
    DEFAULT_AMOUNT = 0
    PRODUCT_PRICE_MAX_DIGITS = 10
    PRODUCT_PRICE_DECIMAL_PLACES = 2
    TOTAL_PRICE_MAX_DIGITS = 10
    TOTAL_PRICE_DECIMAL_PLACES = 2
    DEFAULT_TOTAL_PRICE = 0
    WARRANTY_MAX_LEN = 20
    DEFAULT_WARRANTY = 'No warranty'

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LEN
    )
    customer_name = models.CharField(
        max_length=CUSTOMER_NAME_MAX_LEN
    )
    order_date = models.DateField()
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=StatusChoices.choices
    )
    amount = models.PositiveIntegerField(
        default=DEFAULT_AMOUNT
    )
    product_price = models.DecimalField(
        max_digits=PRODUCT_PRICE_MAX_DIGITS,
        decimal_places=PRODUCT_PRICE_DECIMAL_PLACES
    )
    total_price = models.DecimalField(
        max_digits=TOTAL_PRICE_MAX_DIGITS,
        decimal_places=TOTAL_PRICE_DECIMAL_PLACES,
        default=DEFAULT_TOTAL_PRICE
    )
    warranty = models.CharField(
        max_length=WARRANTY_MAX_LEN,
        default=DEFAULT_WARRANTY
    )
    delivery = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Order #{self.id} - {self.customer_name}'
