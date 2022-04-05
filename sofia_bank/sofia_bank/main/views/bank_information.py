from django.views import generic as views


class AboutUsView(views.TemplateView):
    template_name = 'main/about_us.html'


class ContactView(views.TemplateView):
    template_name = 'main/contacts.html'

