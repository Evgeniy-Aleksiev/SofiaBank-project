from django import forms


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


def get_total_loans_by_type(loan):
    consumer_loan_interest_rate = 0.053
    house_loan_interest_rate = 0.045
    mortgage_loan_interest_rate = 0.034

    loan_type = loan.type
    amount = int(loan.amount)
    period = int(loan.period)

    if loan_type == 'Consumer Loans':
        loan.amount = amount + (amount * consumer_loan_interest_rate * period)

    elif loan_type == 'House Loans':
        loan.amount += amount + (amount * house_loan_interest_rate * period)

    elif loan_type == 'Mortgage Loans':
        loan.amount += amount + (amount * mortgage_loan_interest_rate * period)

    return loan


def deposit_a_loan(deposit_amount, loan_obj, user):
    loan_amount = float(loan_obj.amount)
    if deposit_amount < loan_amount:
        loan_obj.amount = loan_amount - deposit_amount
        loan_obj.save()
        user.loan_amount += deposit_amount
        user.save()

    elif deposit_amount >= loan_amount:
        user.loan_amount += loan_amount
        user.save()
        loan_obj.delete()


