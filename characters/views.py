from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from django.core.urlresolvers import reverse

from forms import CreateCharacterForm

from django.contrib.auth.models import User
from characters.models import Character
from elements.models import GeneralGameStats



# Example: /12/characters/
# Views: All characters the user owns, and a way to choose one to log in

def user_characters(request, user_id):
	characters = Character.objects.filter(user=user_id)
	user = User.objects.get(id=user_id)
	#print user
	return render_to_response('characters.html', 
							{'characters': characters, "user": user}, 
							context_instance=RequestContext(request))
	

def create_character(request, user_id):
	user = User.objects.get(id=user_id)
	
	# Check if max characters has been reached
	chars = Character.objects.filter(user = user_id).count()
	max_chars = GeneralGameStats.objects.get(id=1).maximum_characters
	
	if chars < max_chars:
	
	#Create a new character
		if request.POST:
			new_char_form = CreateCharacterForm(request.POST)


			if new_char_form.is_valid():
				#save form with commit=False
				new_char_obj = new_char_form.save(commit=False)
				#set user and save
				new_char_obj.user = user
				new_char_obj.save()
				
				#adding subtables
				Character.create_factions(new_char_obj)

				return HttpResponseRedirect(reverse('user_characters', args=[user.id]))

			else:
				return render_to_response('create.html', 
								{"user": user, 'create_char': new_char_form}, 
								context_instance=RequestContext(request))
								
		else:
			create_char = CreateCharacterForm
			return render_to_response('create.html', 
								{"user": user, 'create_char': create_char, }, 
								context_instance=RequestContext(request))
		
	# Inform user about max char	
	else:
		check = True
		return render_to_response('create.html',
							{"user": user, 'check': check},
							context_instance=RequestContext(request))

	
	
	
	
	

