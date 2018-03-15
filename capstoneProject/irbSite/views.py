from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	#return HttpResponse('Home page works!!!')
	return render(request, 'irbSite/irb_login.html')
