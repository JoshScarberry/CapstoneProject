
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from irbSite.forms import IndexForm, UserRegisterForm, ProjectForm, AdminForm
from irbSite.models import Project, User



# Create your views here.
#class LoginView

class Index(LoginRequiredMixin,ListView):
    template_name = 'irbSite/index.html'
    form_class = IndexForm

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class Registration(CreateView):
    template_name = 'irbSite/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('irbSite:login')


class Form(LoginRequiredMixin,CreateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    # https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Form, self).form_valid(form)


class EditProject(LoginRequiredMixin, UpdateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    # working for 1 project object
    def get_object(self):
        return Project.objects.get(user=self.request.user)

    #def get_object(self):
    #    return Project.objects.get(pk=self.request.user)

    #def get_object(self, queryset=get_queryset):
    #    return self.request.user

    #def get_object(self, *args, **kwargs):
    #    user = get_object(User, pk=self.kwargs['pk'])
    #    return user.userprofile

class IrbAdmin(LoginRequiredMixin, TemplateView):
    template_name = 'irbSite/admin_forms.html'
    form_class = AdminForm

    def get_queryset(self):
        return Project.objects.filter(is_complete=True)

#https://stackoverflow.com/questions/12187751/django-pass-multiple-models-to-one-template
    #queryset = Project.objects.filter(is_complete=True)

    #def users(self):
    #    return User.objects.all()

    #def get_context_data(self, **kwargs):
        #context = super(IrbAdmin, self).get_context_data(**kwargs)
        #context['user'] = User.objects.filter(id=project.request.user)
        #context['user'] = User.objects.filter(id__id=Project.objects.filter(is_complete=True))
        #return context



class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'irbSite/test.html'
