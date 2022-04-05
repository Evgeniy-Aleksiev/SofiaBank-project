from django.contrib import admin

from sofia_bank.main.models import BankLoans, BankSavings


@admin.register(BankLoans)
class BankLoansAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount')


@admin.register(BankSavings)
class BankSavingsAdmin(admin.ModelAdmin):
    list_display = ('types', 'amount')