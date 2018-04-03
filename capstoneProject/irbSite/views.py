
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, View
from . import forms


# Create your views here.

class Index(TemplateView):
    template_name = 'irbSite/index.html'
    form_class = forms.IndexForm


class Registration(CreateView):
    template_name = 'irbSite/register.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('irbSite:login')

class TestPage(TemplateView):
    template_name = 'irbSite/test.html'

#class Form(TeplateView):
#    template_name = 'irbSite/form.html'
#    form_class = ''
#    success_url = ''
