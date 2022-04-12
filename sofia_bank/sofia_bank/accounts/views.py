from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from sofia_bank.accounts.forms import CreateProfileForm, DeleteProfileForm
from sofia_bank.accounts.models import Profile
from sofia_bank.main.models import BankLoans


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_mixin.LoginRequiredMixin, auth_views.LogoutView):
    pass


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return redirect(self.success_url)


class ProfileDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    fields = ('mobile_number', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user.id})


class ProfileDeleteView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Profile
    template_name = 'accounts/profile_delete.html'
    form_class = DeleteProfileForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loan = list(BankLoans.objects.filter(user_id=self.object.user_id))
        context.update({
            'loan': loan,
        })

        return context
