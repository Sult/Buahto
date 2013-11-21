from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf

from forms import RegistrationForm



# account views
# Register new user
def register_user(request):
	# False till someone fills in and sends
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/users/register_success")
	else:
		form = RegistrationForm()
	
	return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
	

# Registers new user succesfull
def register_success(request):
	return render_to_response("register_success.html")	


# login
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)
	

# authentication
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	
	#returns None if not correct
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/users/loggedin')
	else:
		return HttpResponseRedirect('/users/invalid')


# Logged in
def loggedin(request):
	return render_to_response('loggedin.html',
							{'username': request.user.username})


#invalid login
def invalid_login(request):
	return render_to_response('invalid_login.html')


#Logout
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
	


