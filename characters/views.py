from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from characters.models import Character, CharacterAttribute, FactionReputation
from elements.models import GameRelatedNumbers

from forms import CreateCharacterForm

import datetime
from game_logic import character_logic

# Example: /characters/
# Views: All characters the user owns, and a way to choose one to log in

def characters(request):
	characters = Character.objects.filter(user=request.user.is_authenticated())
	print characters
	return render(request, 'characters.html', {'characters': characters})


# Views character
# Full profile if the user_id is active user, else public profile
def character_profile(request, character_name):
	character = Character.objects.get(name=character_name)
	
	return render(request, 'character.html', {'character': character})
	


#Create a new character	
def create_character(request):
	# Check if max characters has been reached
	
	chars = Character.objects.filter(id=request.user.id).count()
	max_chars = GameRelatedNumbers.objects.get(id=1).maximum_characters
	
	if chars < max_chars:
	
	#Create a new character
		if request.POST:
			new_char_form = CreateCharacterForm(request.POST)


			if new_char_form.is_valid():
				#save form with commit=False
				new_char_obj = new_char_form.save(commit=False)
				#set user and save
				new_char_obj.name = new_char_obj.name.lower()
				new_char_obj.user = request.user
				new_char_obj.remap = datetime.datetime.now()
				new_char_obj.bonus_remaps = GameRelatedNumbers.objects.get(id=1).remap_bonus
				new_char_obj.save()
				
				#adding subtables
				#Character.create_factions(new_char_obj)
				character_logic.create_character(new_char_obj)


				return HttpResponseRedirect(reverse('characters'))

			else:
				return render_to_response('create.html', 
								{'create_char': new_char_form}, 
								context_instance=RequestContext(request))
								
		else:
			create_char = CreateCharacterForm
			return render_to_response('create.html', 
								{'create_char': create_char}, 
								context_instance=RequestContext(request))
		
	# Inform user about max char	
	else:
		check = True
		return render_to_response('create.html',
							{'check': check},
							context_instance=RequestContext(request))


def login_character(request, character_name):
	request.session['character'] = Character.objects.get(name=character_name)
	print request.session['character'].faction
	
	
	return HttpResponseRedirect(reverse('index'))
