# basically create a real simple view for the home page
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'
    # Linking to urls.py
