from django import forms

from sofia_bank.common_files.helpers import BootstrapFormMixin, deposit_a_loan, get_total_loans_by_type
from sofia_bank.main.models import BankLoans, BankSavings, Feedback

LOAN_FIELDS = ('type', 'amount', 'period')
SAVING_FIELDS = ('types', 'amount')


class CreateLoanForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        loan = super().save(commit=False)
        loan.user = self.user
        if commit:
            loan = get_total_loans_by_type(loan)
            loan.save()
        return loan

    class Meta:
        model = BankLoans
        fields = LOAN_FIELDS


class CreateSavingForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        savings = super().save(commit=False)
        savings.user = self.user
        if commit:
            savings.save()
            if savings.types == 'Deposit':
                amount = savings.amount
                loan = BankLoans.objects.filter(user=self.user)[0]
                deposit_a_loan(amount, loan, self.user)

        return savings

    class Meta:
        model = BankSavings
        fields = SAVING_FIELDS


class FeedbackForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Feedback
        fields = '__all__'

