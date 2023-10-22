import os
import django

from main_app.models import ArtworkGallery, Laptop, LaptopBrandChoices, LaptopOperationSystemChoices, ChessPlayer, Meal, \
    Dungeon, Workout

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ready_to_use_django_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries


# Task 1
def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{highest_rated_art.art_name} is the highest-rated art with a {highest_rated_art.rating} rating!'


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# Task 2
def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', 'id').first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(*args):
    laptops_to_create = list(args)
    Laptop.objects.bulk_create(laptops_to_create)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=[LaptopBrandChoices.ASUS, LaptopBrandChoices.LENOVO]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=[LaptopBrandChoices.APPLE, LaptopBrandChoices.DELL, LaptopBrandChoices.ACER]).update(memory=16)


def update_operation_systems():
    (Laptop.objects.filter(brand=LaptopBrandChoices.ASUS).
     update(operation_system=LaptopOperationSystemChoices.WINDOWS))
    (Laptop.objects.filter(brand=LaptopBrandChoices.APPLE).
     update(operation_system=LaptopOperationSystemChoices.MACOS))
    (Laptop.objects.filter(brand__in=[LaptopBrandChoices.DELL, LaptopBrandChoices.ACER]).
     update(operation_system=LaptopOperationSystemChoices.LINUX))
    (Laptop.objects.filter(brand=LaptopBrandChoices.LENOVO).
     update(operation_system=LaptopOperationSystemChoices.CHROME_OS))


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


# Task 3
def bulk_create_chess_players(*args):
    [ChessPlayer.objects.bulk_create(player) for player in list(args)]


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(
        rating__gte=2300,
        rating__lte=2399
    ).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(
        rating__gte=2200,
        rating__lte=2299
    ).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(
        rating__gte=0,
        rating__lte=2199
    ).update(title='regular player')


# Task 4
def get_all_meals():
    return Meal.objects.all()


def set_new_chefs():
    all_meals = get_all_meals()
    for meal in all_meals:
        if meal.meal_type == "Breakfast":
            meal.chef = "Gordon Ramsay"
        elif meal.meal_type == "Lunch":
            meal.chef = "Julia Child"
        elif meal.meal_type == "Dinner":
            meal.chef = "Jamie Oliver"
        elif meal.meal_type == "Snack":
            meal.chef = "Thomas Keller"

        meal.save()


def set_new_preparation_times():
    all_meals = get_all_meals()
    for meal in all_meals:
        if meal.meal_type == "Breakfast":
            meal.preparation_time = '10 minutes'
        elif meal.meal_type == "Lunch":
            meal.preparation_time = '12 minutes'
        elif meal.meal_type == "Dinner":
            meal.preparation_time = '15 minutes'
        elif meal.meal_type == "Snack":
            meal.preparation_time = '5 minutes'

        meal.save()


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=('Breakfast', 'Dinner')).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=('Lunch', 'Snack')).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=('Lunch', 'Snack')).delete()


# Task 5
def get_all_dungeons():
    return Dungeon.objects.all()


def show_hard_dungeons():
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard')
    return '\n'.join([f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!'
                      for dungeon in hard_dungeons])


def bulk_create_dungeons(*args):
    [Dungeon.objects.bulk_create(dungeon) for dungeon in list(args)]


def update_dungeon_names():
    all_dungeons = get_all_dungeons()
    for dungeon in all_dungeons:
        if dungeon.difficulty == 'Easy':
            dungeon.name = 'The Erased Thombs'
        elif dungeon.difficulty == 'Medium':
            dungeon.name = 'The Coral Labyrinth'
        elif dungeon.difficulty == 'Hard':
            dungeon.name = 'The Lost Haunt'

        dungeon.save()


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    all_dungeons = get_all_dungeons()
    for dungeon in all_dungeons:
        if dungeon.difficulty == 'Easy':
            dungeon.recommended_level = 25
        elif dungeon.difficulty == 'Medium':
            dungeon.recommended_level = 50
        elif dungeon.difficulty == 'Hard':
            dungeon.recommended_level = 75

        dungeon.save()


def update_dungeon_rewards():
    dungeons = get_all_dungeons()
    for dungeon in dungeons:
        if dungeon.boss_health == 500:
            dungeon.reward = '1000 Gold'
        if dungeon.location.startswith('E'):
            dungeon.reward = 'New dungeon unlocked'
        if dungeon.location.endswith('s'):
            dungeon.reward = 'Dragonheart Amulet'

        dungeon.save()


def set_new_locations():
    dungeons = get_all_dungeons()
    for dungeon in dungeons:
        if dungeon.recommended_level == 25:
            dungeon.location = 'Enchanted Maze'
        elif dungeon.recommended_level == 50:
            dungeon.location = 'Grimstone Mines'
        elif dungeon.recommended_level == 75:
            dungeon.location = 'Shadowed Abyss'

        dungeon.save()


# Task 6
def show_workouts():
    workouts = (Workout.objects.filter(workout_type__in=('Calisthenics', 'CrossFit')).
                values('name', 'workout_type', 'difficulty'))

    return "\n".join([f"{workout['name']} from {workout['workout_type']} type has {workout['difficulty']} difficulty!"
                      for workout in workouts])


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors():
    instructors_mapping = {
        'Cardio': 'John Smith',
        'Strength': 'Michael Williams',
        'Yoga': 'Emily Johnson',
        'CrossFit': 'Sarah Davis',
        'Calisthenics': 'Chris Heria'
    }

    for workout_type, instructor in instructors_mapping.items():
        Workout.objects.filter(workout_type=workout_type).update(instructor=instructor)


def set_new_duration_times():
    duration_mapping = {
        'John Smith': '15 minutes',
        'Sarah Davis': '30 minutes',
        'Chris Heria': '45 minutes',
        'Michael Williams': '1 hour',
        'Emily Johnson': '1 hour and 30 minutes'
    }

    for instructor, duration in duration_mapping.items():
        Workout.objects.filter(instructor=instructor).update(duration=duration)


def delete_workouts():
    Workout.objects.exclude(workout_type__in=('Strength', 'Calisthenics')).delete()
