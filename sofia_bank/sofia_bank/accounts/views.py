from django.contrib.auth import views as auth_views, authenticate, login, get_user_model
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from sofia_bank.accounts.forms import CreateProfileForm, DeleteProfileForm
from sofia_bank.accounts.models import Profile
from sofia_bank.main.models import BankLoans

UserModel = get_user_model()


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


    # def form_valid(self, form):
    #     user = form.save(commit=True)
    #     current_site = get_current_site(self.request)
    #     mail_subject = 'Activate your account.'
    #     message = render_to_string('authentication/activate_email.html', {
    #         'user': user,
    #         'domain': current_site,
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': default_token_generator.make_token(user),
    #     })
    #     to_email = form.cleaned_data.get('email')
    #     email = EmailMessage(
    #         mail_subject, message, to=[to_email]
    #     )
    #     email.send()
    #     return render(self.request, 'authentication/activation_need.html')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_mixin.LoginRequiredMixin, auth_views.LogoutView):
    pass


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

#
# def activate_user(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = UserModel.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_email_verified = True
#         user.save()
#         return redirect(reverse('login user'))
#     else:
#             return render(request, 'authentication/activation_invalid.html')