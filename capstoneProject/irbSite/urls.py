from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.core.urlresolvers import reverse_lazy

#///////////////MEDIA IMPORT////////////////////////////
from django.conf import settings
from django.views.static import serve

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

    url(r'^project_forms/', views.project_forms,name='project_forms'),

    url(r'^test/', views.TestPage.as_view(),name='test'),

    url(r'^viewforms/(?P<path>\d+)/', views.ViewForms,name='viewforms'),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
