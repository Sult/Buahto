from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm



def index(request):
    """Logs a user into the application."""
    auth_form = AuthenticationForm(None, request.POST or None)
	
    # The form itself handles authentication and checking to make sure passowrd and such are supplied.
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        return HttpResponseRedirect(reverse('characters'))
 
    return render(request, 'index.html', {'auth_form': auth_form})


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


#Logout
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('index'))
	
