from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	#url(r'^$', views.home),
	url(r'^$', login, {'template_name': 'irbSite/login.html'}),
	path('form.html', views.form),
	path('register.html', views.register),
	path('reset_login.html', views.reset_login),
	path('admin.html', views.admin),
	path('confirmation.html', views.confirmation),
	path('admin_description', views.admin_description),
	path('admin_forms.html', views.admin_forms),
	path('admin_index.html', views.admin_index),
	path('index.html', views.index),
	path('project_forms.html', views.project_forms),
	path('user.html', views.user),
	path('user_description.html', views.user_description),
	path('user_forms.html', views.user_forms)


]
