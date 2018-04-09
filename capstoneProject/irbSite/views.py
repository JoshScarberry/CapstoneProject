
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from irbSite.forms import IndexForm, UserRegisterForm, ProjectForm, AdminForm
from irbSite.models import Project, User



# Create your views here.

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Form, self).form_valid(form)


class EditProject(LoginRequiredMixin, UpdateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    queryset = Project.objects.all()
    def edit_object(queryset, pk):
        editPK = get_object_or_404(Project, id=pk)
        project_list = Project.objects.filter(project_id=editPK)


class IrbAdmin(LoginRequiredMixin, ListView):
    template_name = 'irbSite/admin_forms.html'
    form_class = AdminForm

    def get_context_data(self, **kwargs):
        context = super(MultipleModelView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(is_comlete=True)
        context['user'] = User.objects.all()
        return context

    #def get_queryset(self):
    #    return Project.objects.filter(is_complete=True)

#https://stackoverflow.com/questions/12187751/django-pass-multiple-models-to-one-template
    #queryset = Project.objects.filter(is_complete=True)
    #def get_user_names(queryset):
    #    userNames = User.objects.filter(id=querryset.user)

    #def users(self):
    #    return User.objects.all()

    #def get_context_data(self, **kwargs):
        #context = super(IrbAdmin, self).get_context_data(**kwargs)
        #context['user'] = User.objects.filter(id=project.request.user)
        #context['user'] = User.objects.filter(id__id=Project.objects.filter(is_complete=True))
        #return context



class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'irbSite/test.html'
