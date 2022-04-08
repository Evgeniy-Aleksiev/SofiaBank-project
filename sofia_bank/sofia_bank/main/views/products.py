from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from sofia_bank.accounts.models import Profile
from sofia_bank.main.forms import CreateLoanForm, CreateSavingForm
from sofia_bank.main.models import BankLoans


class ProductsAndServicesView(views.TemplateView):
    template_name = 'main/products_and_services.html'


class CreateLoanView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'products/loans.html'
    form_class = CreateLoanForm

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.object.user.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class LoanDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'products/loan_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_loans = list(BankLoans.objects.filter(user_id=self.object.user_id))

        context.update({
            'user_loans': user_loans,
        })

        return context


class CreateSavingView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'products/savings_and_deposits.html'
    form_class = CreateSavingForm

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.object.user.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class NeedsView(views.TemplateView):
    template_name = 'main/customer_needs.html'

