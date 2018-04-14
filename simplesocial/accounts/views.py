from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView


from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm # no instantiation ()
    success_url = reverse_lazy('login') # on successful signup this returns the user to the signup page.  Uses reverse lazy so that it doesn't submit before the user hits submitself.
    template_name = 'accounts/signup.html'
