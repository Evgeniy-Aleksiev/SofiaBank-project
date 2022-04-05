from django.views import generic as views

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


