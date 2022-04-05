from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
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




