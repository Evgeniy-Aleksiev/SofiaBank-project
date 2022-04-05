from datetime import date

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_only_numbers(value):
    for num in value:
        if not num.isdigit():
            raise ValidationError('Value must contain only numbers')


def validate_age(value):
    day_of_birth = value
    today = date.today()
    if (today.year - day_of_birth.year) < 18:
        raise ValidationError('You must be at least 18 years old to register.')