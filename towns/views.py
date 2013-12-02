from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from towns.models import TrainingGround
from characters.models import SkillTrainingTimer
from elements.models import Skill

from game_methods import town_logic, character_logic


def trainingground(request):
	ground_skills_available = town_logic.trainingground_get_skills(request.session['character'].town.trainingground)
	return render(request, 'trainingground.html', {
								'ground_skills_available': ground_skills_available,
								})

def training(request):
	char_skills_available = town_logic.trainingground_get_character_skills(
														request.session['character'], 
														request.session['character'].town.trainingground,
														)
	if request.POST:
		skill_obj = Skill.objects.get(name=request.POST.get('skill'))
		character_logic.train_skill(request.session['character'], skill_obj)
		return HttpResponseRedirect(reverse('index'))

			
	return render(request, 'training.html', {
								'char_skills_available': char_skills_available,
								})
