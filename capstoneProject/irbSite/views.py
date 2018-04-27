
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from irbSite.forms import IndexForm, UserRegisterForm, ProjectForm, AdminForm, ProjectReviewForm
from irbSite.models import Project, User




# Create your views here.
#/////////////////////////////////////////////////// view for login page///////////////////////////////////////////////////////////////////
class Index(LoginRequiredMixin, ListView):
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
    success_url = reverse_lazy('irbSite:confirmation')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Form, self).form_valid(form)


#//////////////////////////////////////////////////// View for uppdate project form page///////////////////////////////////////////////////////
class EditProject(LoginRequiredMixin, UpdateView):
    template_name = 'irbSite/form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    def get_queryset(self, queryset=None ):
        valid_object = Project.objects.filter(user=self.request.user, is_complete=False)
        return valid_object


#///////////////////////////////////////////////////// View for admin reviewing complete projects page//////////////////////////////////////////////////
class ReviewProject(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'irbSite/admin_forms.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('irbSite:irbadmin')
    queryset = Project.objects.all()

    #PermissionRequiredMixin
    permission_required = 'user.is_staff == True'
    raise_exception = True

#//////////////////////////////////////////////////// View for submitter to view a complete sumission but cannot edit ////////////////////////////
class CompleteAwaitingReview(LoginRequiredMixin, DetailView):
    template_name = 'irbSite/user_project_review.html'
    form_class = ProjectForm
    success_url = reverse_lazy('irbSite:index')

    def get_queryset(self, queryset=None ):
        return Project.objects.filter(user=self.request.user)


#/////////////////////////////////////////////////////// View for admin viewing completed projects page////////////////////////////////////////////
class IrbAdmin(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'irbSite/admin_index.html'
    queryset=Project.objects.filter(is_complete=True, is_approved=False)

    #PermissionRequiredMixin
    permission_required = 'user.is_staff == True'
    raise_exception = True


#/////////////////////////////////////////////////////// View for downloading document templates ////////////////////////////////////////////////////////
class ProjectFormsView(LoginRequiredMixin, ListView):
    template_name = 'irbSite/project_forms.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('irbSite:irbadmin')

    queryset = Project.objects.all()

#/////////////////////////////////////////////////////// View for a list of previously approved projects ///////////////////////////////////////////////////////////
class ApprovedProjectsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'irbSite/approved_index.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('irbsite:irbadmin')

    queryset = Project.objects.filter(is_complete=True, is_approved=True)

    #PermissionRequiredMixin
    permission_required = 'user.is_staff == True'

#///////////////////////////////////////////////////// View for previously approved projects and the ability to set is_approved to False///////////////////
class ApprovedProjectsUpdatesView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'irbSite/approved_projects.html'
    form_class = ProjectReviewForm
    success_url = reverse_lazy('irbsite:irbadmin')

    queryset = Project.objects.filter(is_approved=True)

    #PermissionRequiredMixin
    permission_required = 'user.is_staff == True'

#//////////////////////////////////////////////////// Succelfull submit page /////////////////////////////////////////////////////////////////////////////
class ConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = 'irbSite/confirmation.html'


#//////////////////////////////////////////////////// View for testing ////////////////////////////////////////////////////////////////////////////////////
#class TestPage(LoginRequiredMixin,TemplateView):
#    template_name = 'irbSite/test.html'
