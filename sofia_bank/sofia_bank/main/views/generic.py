from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.views.decorators.cache import cache_page

from sofia_bank.accounts.models import Profile
from sofia_bank.main.models import BankLoans, BankSavings, ExchangeRates


class HomeView(views.ListView):
    queryset = ExchangeRates.objects.order_by('currency')
    template_name = 'main/home_page.html'
    context_object_name = 'exchanges'


#@cache_page(60)
class DashboardView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'main/dashboard.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_loans = list(BankLoans.objects.filter(user_id=self.object.user_id))
        user_savings = list(BankSavings.objects.filter(user_id=self.object.user_id))

        loans = f"{sum(l.amount for l in user_loans):.2f}"
        deposits = f"{sum(d.amount for d in user_savings if d.types == 'Deposit'):.2f}"
        savings = f"{sum(s.amount for s in user_savings if s.types == 'Savings'):.2f}"

        context.update({
            'total_loans': loans,
            'total_deposits': deposits,
            'total_savings': savings,
            'total_loan_paid': f"{self.object.user.loan_amount:.2f}",
        })

        return context
