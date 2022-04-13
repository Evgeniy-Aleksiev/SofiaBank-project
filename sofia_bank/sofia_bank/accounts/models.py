from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from sofia_bank.accounts.managers import SofiaBankUserManager
from sofia_bank.common_files.validators import validate_only_letters, validate_age, validate_only_numbers


class SofiaBankUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USER_MAX_LEN = 25
    USER_MIN_LEN = 5

    username = models.CharField(
        max_length=USER_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(USER_MIN_LEN),
        )
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    loan_amount = models.FloatField(
        default=0
    )

    USERNAME_FIELD = 'username'

    objects = SofiaBankUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    MIDDLE_NAME_MIN_LENGTH = 2
    MIDDLE_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    middle_name = models.CharField(
        max_length=MIDDLE_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(MIDDLE_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
        validators=(
            MinLengthValidator(10),
            validate_only_numbers,
        )
    )

    email = models.EmailField()

    mobile_number = models.CharField(
        max_length=9,
        validators=(
            MinLengthValidator(8),
            validate_only_numbers,
        )
    )

    date_of_birth = models.DateField(
        validators=(
            validate_age,
        )
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        SofiaBankUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
