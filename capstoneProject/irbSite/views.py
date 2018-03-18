from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	#return HttpResponse('Home page works!!!')

	# example variables
	name = 'madeUpName'
	anything = 'anyvalue'

	# example of args to pass as dictionaries
	args = {'myname': name, 'anyvalue': anything}
	return render(request, 'irbSite/login.html', args)

def form(request):
	return render(request, 'irbSite/form.html')

def register(request):
	return render(request, 'irbSite/register.html')

def reset_login(request):
	return render(request, 'irbSite/reset_login.html')

def admin(request):
	return render(request, 'irbSite/admin.html')

def confirmation(request):
	return render(request, 'irbSite/confirmation.html')

def admin_description(request):
	return render(request, 'irbSite/admin_description.html')

def admin_forms(request):
	return render(request, 'irbSite/admin_forms.html')

def admin_index(request):
	return render(request, 'irbSite/admin_index.html')

def confirmation(request):
	return render(request, 'irbSite/confirmation.html')

def index(request):
	return render(request, 'irbSite/index.html')

def project_forms(request):
	return render(request, 'irbSite/project_forms.html')

def user_description(request):
	return render(request, 'irbSite/user_description.html')

def user_forms(request):
	return render(request, 'irbSite/user_forms.html')

def user(request):
	return render(request, 'irbSite/user.html')
