from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required


app_name = 'irbSite'

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name = 'irbSite/login.html'),name='login'),

    url(r'^logout/',auth_views.LogoutView.as_view(),name='logout'),

    url(r'^password_reset',auth_views.PasswordResetView.as_view(),name='reset'),

    url(r'^register/',views.Registration.as_view(),name='register'),

    url(r'^index/',views.Index.as_view(),name='index'),

    url(r'^form/', views.Form.as_view(), name = 'form'),

    url(r'^edit/(?P<pk>\d+)/', views.EditProject.as_view(), name = 'editProject'),

    url(r'^irbadmin/', views.IrbAdmin.as_view(), name = 'irbadmin'),

    url(r'^review/(?P<pk>\d+)/', views.ReviewProject.as_view(), name = 'reviewProject'),

    url(r'^projectForms/', views.ProjectFormsView.as_view(), name = 'projectForms'),

    url(r'^awaitingReview/(?P<pk>\d+)/', views.CompleteAwaitingReview.as_view(), name = 'completeAwaitingReview'),

    url(r'^notes/(?P<pk>\d+)/', views.NotesToSubmitterView.as_view(), name = 'notesToSubmitter'),

    url(r'^confirmation/', views.ConfirmationView.as_view(),name = 'confirmation'),

    url(r'^approved/', views.ApprovedProjectsListView.as_view(),name = 'approved'),

    url(r'^approvedReview/(?P<pk>\d+)/', views.ApprovedProjectsUpdatesView.as_view(),name = 'approvedReview'),

    #url(r'^test/', views.TestPage.as_view(),name='test'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
