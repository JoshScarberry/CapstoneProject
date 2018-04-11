
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from irbSite.forms import IndexForm, UserRegisterForm, ProjectForm, AdminForm, ProjectReviewForm
from irbSite.models import Project, User
from django.contrib.auth.decorators import login_required



# Create your views here.
#/////////////////////////////////////////////////// view for login page///////////////////////////////////////////////////////////////////
class Index(LoginRequiredMixin,ListView):
    template_name = 'irbSite/index.html'
    form_class = IndexForm

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


#//////////////////////////////////////////////// View for register page///////////////////////////////////////////////////////////////////
class Registration(CreateView):
    template_name = 'irbSite/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('irbSite:login')


#////////////////////////////////////////////// View for new project form page////////////////////////////////////////////////////////////////
class Form(LoginRequiredMixin,CreateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Form, self).form_valid(form)


#//////////////////////////////////////////////////// View for uppdate project form page///////////////////////////////////////////////////////
class EditProject(LoginRequiredMixin, UpdateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    queryset = Project.objects.all()
    #def edit_object(queryset, pk):
        #editPK = get_object_or_404(Project, id=pk)
        #project_list = Project.objects.filter(project_id=editPK)
        #pass

#///////////////////////////////////////////////////// View for admin reviewing complete projects page//////////////////////////////////////////////////
class ReviewProject(LoginRequiredMixin, DetailView):
    template_name = 'irbSite/admin_forms.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('irbSite:irbadmin')


    queryset = Project.objects.all()
    #def edit_object(queryset, pk):
        #editPK = get_object_or_404(Project, id=pk)
        #project_list = Project.objects.filter(project_id=editPK)
        #print(project_list)
        #pass

    #return render(request, 'irbSite/admin_forms.html' ,{
    #    'answers' : answers,
    #})

#/////////////////////////////////////////////////////// View for admin viewing completed projects page////////////////////////////////////////////
class IrbAdmin(LoginRequiredMixin, ListView):
    template_name = 'irbSite/admin_index.html'
    #form_class = AdminForm
    model = Project
    #model = User


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.filter(is_complete=True)
        context['user_list'] = User.objects.all()
        print(context)
        return context



class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'irbSite/test.html'

@login_required(login_url="/accounts/login/")
def project_forms(request):
    return render(request, 'irbSite/project_forms.html')
