from django.contrib import admin

from sofia_bank.main.models import BankLoans, BankSavings, AtmAndBranches, Feedback, ExchangeRates


@admin.register(BankLoans)
class BankLoansAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount')


@admin.register(BankSavings)
class BankSavingsAdmin(admin.ModelAdmin):
    list_display = ('types', 'amount')


@admin.register(AtmAndBranches)
class AtmsAndBranchesAdmin(admin.ModelAdmin):
    list_display = ('bank_or_atm_number', 'city', 'branches_and_atms')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('bank_or_atm_number', 'username', 'date', 'happy', 'details')
    list_filter = ('date', )


@admin.register(ExchangeRates)
class ExchangeRatesAdmin(admin.ModelAdmin):
    list_display = ('date', 'currency', 'fixing', 'buy', 'sell', 'currency_units')


