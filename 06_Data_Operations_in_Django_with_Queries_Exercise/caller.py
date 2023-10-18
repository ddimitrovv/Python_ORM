import os
import django

from main_app.models import Pet, Artifact, Location, Car, Task

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def create_pet(name, species):
    Pet.objects.create(name=name, species=species)
    return f'{name} is a very cute {species}!'


def create_artifact(name, origin, age, description, is_magical):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f'The artifact {name} is {age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    locations_info = [f"{location.name} has a population of {location.population}!" for location in locations]
    return "\n".join(locations_info)


def new_capital():
    first_location = Location.objects.first()
    if first_location:
        first_location.is_capital = True
        first_location.save()


def get_capitals():
    capitals = Location.objects.filter(is_capital=True).values('name')
    return capitals


def delete_first_location():
    first_location = Location.objects.first()
    if first_location:
        first_location.delete()


def apply_discount():
    all_cars = Car.objects.all()
    for car in all_cars:
        discount = 1 - sum(int(x) for x in str(car.year)) / 100
        total_amount = float(car.price) * discount
        car.price_with_discount = total_amount
        car.save()


def get_recent_cars():
    wanted_cars = Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')
    return wanted_cars


def delete_last_car():
    last_car = Car.objects.last()
    if last_car:
        last_car.delete()


def show_unfinished_tasks():
    wanted_tasks = [f'Task - {task.title} needs to be done until {task.due_date}!'
                    for task in Task.objects.filter(is_finished=False)]
    return '\n'.join(wanted_tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        task.is_finished = True if task.pk % 2 != 0 else task.is_finished
        task.save()


def encode_and_replace(text, task_title):
    encoded_text = ''
    for char in text:
        encoded_text += chr(ord(char) - 3)
    tasks_with_same_title = Task.objects.filter(title=task_title)
    for task in tasks_with_same_title:
        task.description = encoded_text
        task.save()
