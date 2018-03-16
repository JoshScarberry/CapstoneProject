from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	#return HttpResponse('Home page works!!!')

	# example variables
	name = 'madeUpName'
	anything = 'anyvalue'

	# example of args to pass as dictionaries
	args = {'myname': name, 'anyvalue': anything}
	return render(request, 'irbSite/irb_login.html', args)

def irb_form(request):
	return render(request, 'irbSite/irb_form.html')

def irb_register(request):
	return render(request, 'irbSite/irb_register.html')

def irb_reset(request):
	return render(request, 'irbSite/irb_reset.html')

def admin(request):
	return render(request, 'irbSite/admin.html')

def confirmation(request):
	return render(request, 'irbSite/confirmation.html')
