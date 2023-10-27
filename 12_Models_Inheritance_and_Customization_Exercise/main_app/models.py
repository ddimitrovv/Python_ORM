from abc import abstractmethod
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models


# Task 1
class BaseCharacter(models.Model):
    NAME_MAX_LEN = 100

    class Meta:
        abstract = True

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    description = models.TextField()

    @abstractmethod
    def __str__(self):
        ...


class Mage(BaseCharacter):
    ELEMENTAL_POWER_MAX_LEN = 100
    SPELLBOOK_TYPE_MAX_LEN = 100

    elemental_power = models.CharField(
        max_length=ELEMENTAL_POWER_MAX_LEN
    )
    spellbook_type = models.CharField(
        max_length=SPELLBOOK_TYPE_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class Assassin(BaseCharacter):
    WEAPON_TYPE_MAX_LEN = 100
    ASSASSINATION_TECHNIQUE_MAX_LEN = 100

    weapon_type = models.CharField(
        max_length=WEAPON_TYPE_MAX_LEN
    )
    assassination_technique = models.CharField(
        max_length=ASSASSINATION_TECHNIQUE_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class DemonHunter(BaseCharacter):
    WEAPON_TYPE_MAX_LEN = 100
    DEMON_SLAYING_ABILITY_MAX_LEN = 100

    weapon_type = models.CharField(
        max_length=WEAPON_TYPE_MAX_LEN
    )
    demon_slaying_ability = models.CharField(
        max_length=DEMON_SLAYING_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class TimeMage(Mage):
    TIME_MAGIC_MASTERY_MAX_LEN = 100
    TEMPORAL_SHIFT_ABILITY_MAX_LEN = 100

    time_magic_mastery = models.CharField(
        max_length=TIME_MAGIC_MASTERY_MAX_LEN
    )
    temporal_shift_ability = models.CharField(
        max_length=TEMPORAL_SHIFT_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class Necromancer(Mage):
    RAISE_DEAD_ABILITY_MAX_LEN = 100

    raise_dead_ability = models.CharField(
        max_length=RAISE_DEAD_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class ViperAssassin(Assassin):
    VENOMOUS_SHIFT_ABILITY_MAX_LEN = 100
    VENOMOUS_BITE_ABILITY_MAX_LEN = 100

    venomous_strikes_mastery = models.CharField(
        max_length=VENOMOUS_SHIFT_ABILITY_MAX_LEN
    )
    venomous_bite_ability = models.CharField(
        max_length=VENOMOUS_BITE_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class ShadowbladeAssassin(Assassin):
    SHODOWSTEP_ABILITY_MAX_LEN = 100

    shadowstep_ability = models.CharField(
        max_length=SHODOWSTEP_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class VengeanceDemonHunter(DemonHunter):
    VENGEANCE_ABILITY_MAX_LEN = 100
    RETRIBUTION_ABILITY_MAX_LEN = 100

    vengeance_mastery = models.CharField(
        max_length=VENGEANCE_ABILITY_MAX_LEN
    )
    retribution_ability = models.CharField(
        max_length=RETRIBUTION_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


class FelbladeDemonHunter(DemonHunter):
    FELBLADE_ABILITY_MAX_LEN = 100

    felblade_ability = models.CharField(
        max_length=FELBLADE_ABILITY_MAX_LEN
    )

    def __str__(self):
        return self.__class__.__name__


# Task 2
class UserProfile(models.Model):
    USERNAME_MAX_LEN = 70

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )


class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    is_read = models.BooleanField(
        default=False
    )

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def mark_as_unread(self):
        self.is_read = False
        self.save()

    def reply_to_message(self, reply_content, receiver):
        new_message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=reply_content
        )
        new_message.save()
        return new_message

    def forward_message(self, sender, receiver):
        forwarded_message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=self.content
        )
        forwarded_message.save()
        return forwarded_message


# Task 3
class StudentIDField(models.PositiveIntegerField):
    ERROR_MESSAGE = 'Invalid Student ID. Must be a positive integer.'

    def to_python(self, value):
        if isinstance(value, int):
            return value
        try:
            value = int(value)
            if value < 0:
                raise ValueError(self.ERROR_MESSAGE)
        except (ValueError, TypeError):
            raise ValidationError(self.ERROR_MESSAGE)
        return value


class Student(models.Model):
    NAME_MAX_LEN = 100
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    student_id = StudentIDField()


# Task 4
class MaskedCreditCardField(models.CharField):
    # Credit card number in masked format (****-****-****-XXXX)

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, value):

        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        if not value.isdigit():
            raise ValidationError("The card number must contain only digits")
        if len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")

        return "****-****-****-" + value[-4:]


class CreditCard(models.Model):
    CARD_OWNER_MAX_LEN = 100
    card_owner = models.CharField(
        max_length=CARD_OWNER_MAX_LEN
    )
    card_number = MaskedCreditCardField()

    def __str__(self):
        return self.card_owner


# Task 5
class Hotel(models.Model):
    NAME_MAX_LEN = 100
    ADDRESS_MAX_LEN = 200

    name = models.CharField(
        max_length=NAME_MAX_LEN
    )
    address = models.CharField(
        max_length=ADDRESS_MAX_LEN
    )


class Room(models.Model):
    NUMBER_MAX_LEN = 100
    PRICE_PER_NIGHT_MAX_DIGITS = 10
    PRICE_PER_NIGHT_DECIMAL_PLACES = 2

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE
    )
    number = models.CharField(
        max_length=NUMBER_MAX_LEN,
        unique=True
    )
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(
        max_digits=PRICE_PER_NIGHT_MAX_DIGITS,
        decimal_places=PRICE_PER_NIGHT_DECIMAL_PLACES
    )

    def save(self, *args, **kwargs):
        if self.total_guests > self.capacity:
            raise ValidationError('Total guests are more than the capacity of the room')
        super(Room, self).save(*args, **kwargs)
        return f'Room {self.number} created successfully'


def check_start_date_before_end_date(start_date, end_date):
    # Check if the start date is after or the same as the end date
    if start_date >= end_date:
        raise ValidationError("Start date cannot be after or in the same end date")


def check_for_overlapping_reservations(room, start_date, end_date, reservation_type, type):
    # Check for overlapping reservations
    reservation_types = {
        'RegularReservation': RegularReservation,
        'SpecialReservation': SpecialReservation
    }

    error_types = {
        'reservation': f'Room {room.number} cannot be reserved',
        'extend': 'Error during extending reservation'
    }

    overlapping_reservations = reservation_types[reservation_type].objects.filter(
        room=room,
        start_date__lte=end_date,
        end_date__gte=start_date
    )

    if overlapping_reservations.exists():
        raise ValidationError(error_types[type])


class BaseReservation(models.Model):
    class Meta:
        abstract = True

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def reservation_period(self):
        if self.start_date and self.end_date:
            delta = self.end_date - self.start_date
            return delta.days
        return 0

    def calculate_total_cost(self):
        if self.room and self.start_date and self.end_date:
            reservation_period = self.reservation_period()
            if reservation_period > 0:
                return round(self.room.price_per_night * reservation_period, 1)
        return 0.0

    @abstractmethod
    def __str__(self):
        ...


class RegularReservation(BaseReservation):
    def save(self, *args, **kwargs):
        check_start_date_before_end_date(self.start_date, self.end_date)
        check_for_overlapping_reservations(
            self.room,
            self.start_date,
            self.end_date,
            self.__class__.__name__,
            'reservation')

        super(RegularReservation, self).save(*args, **kwargs)

        return f"Regular reservation for room {self.room.number}"

    def __str__(self):
        return self.__class__.__name__


class SpecialReservation(BaseReservation):
    def save(self, *args, **kwargs):
        check_start_date_before_end_date(self.start_date, self.end_date)
        check_for_overlapping_reservations(
            self.room,
            self.start_date,
            self.end_date,
            self.__class__.__name__,
            'reservation'
        )

        super(SpecialReservation, self).save(*args, **kwargs)

        return f"Special reservation for room {self.room.number}"

    def extend_reservation(self, days: int):
        if days <= 0:
            raise ValidationError("Extension days must be a positive integer")

        extended_end_date = self.end_date + timedelta(days=days)
        check_for_overlapping_reservations(
            self.room,
            self.start_date,
            self.end_date,
            self.__class__.__name__,
            'extend'
        )

        self.end_date = extended_end_date
        self.save()

        return f"Extended reservation for room {self.room.number} with {days} days"

    def __str__(self):
        return self.__class__.__name__
