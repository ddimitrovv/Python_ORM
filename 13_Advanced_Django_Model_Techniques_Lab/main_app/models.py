from django.core.exceptions import ValidationError
from django.db import models

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


# Task 1
class Restaurant(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 100
    LOCATION_MIN_LEN = 2
    LOCATION_MAX_LEN = 200
    RATING_MAX_DIGITS = 3
    RATING_DECIMAL_PLACES = 2
    MIN_RATING = 0
    MAX_RATING = 5
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN, f'Name must be at least {NAME_MIN_LEN} characters long.'),
            MaxLengthValidator(NAME_MAX_LEN, f'Name cannot exceed {NAME_MAX_LEN} characters.'),
        ),
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
        validators=(
            MinLengthValidator(LOCATION_MIN_LEN, f'Location must be at least {LOCATION_MIN_LEN} characters long.'),
            MaxLengthValidator(LOCATION_MAX_LEN, f'Location cannot exceed {LOCATION_MAX_LEN} characters.'),
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    rating = models.DecimalField(
        max_digits=RATING_MAX_DIGITS,
        decimal_places=RATING_DECIMAL_PLACES,
        validators=(
            MinValueValidator(MIN_RATING, f'Rating must be at least {MIN_RATING:.2f}.'),
            MaxValueValidator(MAX_RATING, f'Rating cannot exceed {MAX_RATING:.2f}.'),
        ),
    )

    def __str__(self):
        return self.name


# Task 2
def validate_menu_categories(desc):
    # Check if the description includes specific categories
    categories = ["Appetizers", "Main Course", "Desserts"]
    for category in categories:
        if category not in desc:
            all_categories_str = ', '.join([f'"{x}"' for x in categories])
            raise ValidationError(

                f'The menu must include each of the categories {all_categories_str}.'
            )


class Menu(models.Model):
    NAME_MAX_LEN = 100
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    description = models.TextField(
        validators=(
            validate_menu_categories,
        )
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ReviewMixin(models.Model):
    REVIEWER_NAME_MAX_LEN = 100
    MAX_RATING = 5

    class Meta:
        abstract = True
        ordering = ['-rating']
        unique_together = ('reviewer_name', 'restaurant')

    reviewer_name = models.CharField(
        max_length=REVIEWER_NAME_MAX_LEN
    )
    review_content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(MAX_RATING, f'Rating cannot exceed {MAX_RATING}.'),
        ]
    )


# Task 3
class RestaurantReview(models.Model):
    REVIEWER_NAME_MAX_LEN = 100
    MAX_RATING = 5

    class Meta:
        ordering = ['-rating']
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ('reviewer_name', 'restaurant')
        abstract = True

    reviewer_name = models.CharField(
        max_length=REVIEWER_NAME_MAX_LEN
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    review_content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(MAX_RATING),
        )
    )

    def __str__(self):
        return f"{self.reviewer_name}'s Review for {self.restaurant.name}"


class RegularRestaurantReview(RestaurantReview):
    class Meta:
        ordering = ['-rating']
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ('reviewer_name', 'restaurant')


class FoodCriticRestaurantReview(RestaurantReview, ReviewMixin):
    FOOD_CRITIC_CUISINE_AREA_MAX_LEN = 100

    class Meta:
        ordering = ['-rating']
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"
        unique_together = ('reviewer_name', 'restaurant')

    food_critic_cuisine_area = models.CharField(
        max_length=FOOD_CRITIC_CUISINE_AREA_MAX_LEN
    )


# Task 5
class MenuReview(ReviewMixin):

    class Meta:
        ordering = ['-rating']
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ('reviewer_name', 'menu')
        indexes = [
            models.Index(fields=['menu'], name='main_app_menu_review_menu_id'),
        ]

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.reviewer_name}'s Review for {self.menu.name}"
