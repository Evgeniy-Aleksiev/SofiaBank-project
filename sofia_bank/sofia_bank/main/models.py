from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


UserModel = get_user_model()


class BankLoans(models.Model):
    LOANS_MAX_AMOUNT = 200000
    LOANS_MIN_AMOUNT = 1000
    LOANS_MAX_NUMBER_PERIOD = 30
    LOANS_MIN_NUMBER_PERIOD = 1

    CONSUMER_LOANS = 'Consumer Loans'
    HOUSE_LOANS = 'House Loans'
    MORTGAGE_LOANS = 'Mortgage Loans'

    TYPES = [(x, x) for x in (CONSUMER_LOANS, HOUSE_LOANS, MORTGAGE_LOANS)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    amount = models.IntegerField(
        validators=[
            MaxValueValidator(LOANS_MAX_AMOUNT),
            MinValueValidator(LOANS_MIN_AMOUNT),
        ]
    )

    period = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(LOANS_MAX_NUMBER_PERIOD),
            MinValueValidator(LOANS_MIN_NUMBER_PERIOD),
        ]
    )

    loan_date = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class BankSavings(models.Model):
    DEPOSIT_MAX_AMOUNT = 200000
    DEPOSIT_MIN_AMOUNT = 1

    DEPOSIT = 'Deposit'
    SAVINGS = 'Savings'

    TYPES = [(x, x) for x in (DEPOSIT, SAVINGS)]

    types = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    amount = models.IntegerField(
        validators=[
            MaxValueValidator(DEPOSIT_MAX_AMOUNT),
            MinValueValidator(DEPOSIT_MIN_AMOUNT),
        ]
    )

    deposit_date = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class AtmAndBranches(models.Model):
    CITY_MAX_LENGTH = 20
    CITY_MIN_LENGTH = 3
    NEIGHBORHOOD_MAX_LENGTH = 20
    NEIGHBORHOOD_MIN_LENGTH = 3
    STREET_MAX_LENGTH = 30
    STREET_MIN_LENGTH = 3

    ATMS = 'ATMs'
    BRANCHES = 'Branches'

    ASSISTANT = [(x, x) for x in (ATMS, BRANCHES)]

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=(
            MinLengthValidator(CITY_MIN_LENGTH),
        )
    )

    neighborhood = models.CharField(
        max_length=NEIGHBORHOOD_MAX_LENGTH,
        validators=(
            MinLengthValidator(NEIGHBORHOOD_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    street = models.CharField(
        max_length=STREET_MAX_LENGTH,
        validators=(
            MinLengthValidator(STREET_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    branches_and_atms = models.CharField(
        max_length=max(len(x) for x, _ in ASSISTANT),
        choices=ASSISTANT,
    )

    bank_or_atm_number = models.IntegerField(
        primary_key=True,
        unique=True,
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(1000),
        ],
    )

    open_on_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        neighborhood = ''
        street = ''

        if self.neighborhood is not None:
            neighborhood = self.neighborhood

        if self.street is not None:
            street = self.street

        return f'({self.bank_or_atm_number})| {self.city} {neighborhood} {street}'


class Feedback(models.Model):
    USER_MAX_LEN = 25
    USER_MIN_LEN = 5

    username = models.CharField(
        max_length=USER_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(USER_MIN_LEN),
        )
    )

    happy = models.BooleanField()

    details = models.TextField()

    date = models.DateField(auto_now_add=True)

    bank_or_atm_number = models.ForeignKey(
        AtmAndBranches,
        on_delete=models.CASCADE,
    )



