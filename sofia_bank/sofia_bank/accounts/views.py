from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from sofia_bank.accounts.forms import CreateProfileForm, DeleteProfileForm
from sofia_bank.accounts.models import Profile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.object.user.id})


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileEditView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    fields = ('mobile_number', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user.id})


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'accounts/profile_delete.html'
    form_class = DeleteProfileForm

