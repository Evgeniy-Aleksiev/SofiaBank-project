from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from sofia_bank.main.forms import FeedbackForm
from sofia_bank.main.models import AtmAndBranches


class AboutUsView(views.TemplateView):
    template_name = 'main/about_us.html'


class ContactView(views.TemplateView):
    model = AtmAndBranches
    template_name = 'main/contacts.html'
    context_object_name = 'atms_and_branches'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        banks = list(AtmAndBranches.objects.filter(branches_and_atms__contains='Branches'))
        atms = list(AtmAndBranches.objects.filter(branches_and_atms__contains='ATMs'))

        context.update({
            'banks': banks,
            'atms': atms,
        })

        return context


class FeedbackView(views.CreateView):
    template_name = 'main/feedback.html'
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse_lazy('feedback message')


class FeedbackMessageView(views.TemplateView):
    template_name = 'main/feedback_message.html'


