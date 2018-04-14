# basically create a real simple view for the home page
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'
    # Linking to urls.py
