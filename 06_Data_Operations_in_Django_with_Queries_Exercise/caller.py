import os
import django

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character, CharacterChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Task 1
def create_pet(name, species):
    Pet.objects.create(name=name, species=species)
    return f'{name} is a very cute {species}!'


# Task 2
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


# Task 3
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


# Task 4
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


# Task 5
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


# Task 6
def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    output = [f'Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!'
              for room in deluxe_rooms]
    return '\n'.join(output)


def increase_room_capacity():
    rooms = HotelRoom.objects.order_by('id')

    for idx, room in enumerate(rooms):
        if not room.is_reserved:
            continue
        if idx == 0:
            room.capacity += room.id
        elif room.is_reserved:
            room.capacity += rooms[idx - 1].capacity
        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    HotelRoom.objects.last().delete()


# Task 7
def update_characters():
    characters = Character.objects.all()
    for character in characters:
        if character.class_name == 'Mage':
            character.level += 3
        elif character.class_name == 'Warrior':
            character.hit_points /= 2
            character.dexterity += 4
        elif character.class_name in ('Assassin', 'Scout'):
            character.inventory = 'The inventory is empty'
        character.save()

    # Option 2 - you will need: from django.db.models import F
    # Character.objects.filter(class_name='Mage').update(level=F('level') + 3)
    # Character.objects.filter(class_name='Warrior').update(
    #     hit_points=F('hit_points') / 2,
    #     dexterity=F('dexterity') + 4,
    # )
    # Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
    #     inventory='The inventory is empty',
    # )


def fuse_characters(first_character, second_character):

    inventory = ''
    if first_character.class_name in ('Mage', 'Scout'):
        inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    elif first_character.class_name in ('Warrior', 'Assassin'):
        inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=f'{first_character.name} {second_character.name}',
        class_name=CharacterChoices.FUSION,
        level=(first_character.level + second_character.level) // 2,
        strength=int((first_character.strength + second_character.strength) * 1.2),
        dexterity=int((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=int((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.filter(inventory__icontains='The inventory is empty').delete()
