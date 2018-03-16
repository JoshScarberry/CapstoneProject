from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	#url(r'^$', views.home),
	url(r'^$', login, {'template_name': 'irbSite/irb_login.html'}),
	path('irb_form.html', views.irb_form),
	path('irb_register.html', views.irb_register),
	path('irb_reset.html', views.irb_reset),
	path('admin.html', views.admin),
	path('confirmation.html', views.confirmation)


]
