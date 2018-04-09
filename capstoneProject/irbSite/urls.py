from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.core.urlresolvers import reverse_lazy


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
    
    url(r'^test/', views.TestPage.as_view(),name='test'),

]
