import os
from datetime import timedelta, date

import django
from django.db import models
from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import (Author, Book, Artist, Song, Product,
                             Review, Driver, DrivingLicense, Car, Owner, Registration)


# Task 1
def show_all_authors_with_their_books():
    authors_with_books = []
    authors = Author.objects.all().prefetch_related('book_set')

    for author in authors:
        books = author.book_set.all()
        if books:
            book_titles = ", ".join(book.title for book in books)
            authors_with_books.append(f'{author.name} has written - {book_titles}!')

    return "\n".join(authors_with_books)


def delete_all_authors_without_books():
    authors_without_books = Author.objects.annotate(num_books=models.Count('book'))
    authors_without_books = authors_without_books.filter(num_books=0)

    for author in authors_without_books:
        author.delete()


# Task 2
from django.shortcuts import get_object_or_404


def add_song_to_artist(artist_name, song_title):
    artist, created = Artist.objects.get_or_create(name=artist_name)
    song, created = Song.objects.get_or_create(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    songs = artist.songs.all().order_by('-id')

    return songs


def remove_song_from_artist(artist_name, song_title):
    artist = get_object_or_404(Artist, name=artist_name)
    song = get_object_or_404(Song, title=song_title)

    artist.songs.remove(song)


# Task 3
def calculate_average_rating_for_product_by_name(product_name):
    reviews = Review.objects.filter(product=Product.objects.filter(name=product_name).get())
    if reviews:
        average = sum([x.rating for x in reviews]) / len(reviews)
        return average


def get_reviews_with_high_ratings(threshold):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    products = Product.objects.filter(reviews__isnull=True).order_by('-name')
    return products


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


# Task 4
def get_all_driving_license():
    return DrivingLicense.objects.all()


def calculate_licenses_expiration_dates():
    licenses = get_all_driving_license()
    expiration_dates = []

    for license in licenses:
        expiration_date = license.issue_date + timedelta(days=365)
        expiration_dates.append(f"License with id: {license.license_number} expires on {expiration_date}!")

    expiration_dates.sort(reverse=True)
    return '\n'.join(expiration_dates)


def get_drivers_with_expired_licenses(due_date):
    drivers_with_expired_license = []
    licenses = get_all_driving_license()

    for license in licenses:
        if license.issue_date + timedelta(days=365) > due_date:
            drivers_with_expired_license.append(license.driver)

    return drivers_with_expired_license


# Task 5
def register_car_by_owner(owner):
    try:
        registration = Registration.objects.filter(car__isnull=True).first()
        car = Car.objects.filter(registration__isnull=True).first()

        if registration and car:
            car.registration = registration
            registration.registration_date = date.today()
            car.save()
            registration.save()

            return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
        else:
            return "No available registration or car for this owner."
    except Exception as e:
        return str(e)
