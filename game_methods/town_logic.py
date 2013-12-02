# TODO: fix skill requirements in get_character_traininggrounds_skills

from django.core.exceptions import ObjectDoesNotExist

from towns.models import TrainingGround, TrainingCategory
from elements.models import Skill
from characters.models import TrainedSkill, SkillTrainingTimer



#give a (nested) list of all possible categories with their posisble skills
def trainingground_get_skills(trainingground_obj):
	"""
	Get all available skills you can train at current trainingground 
	"""
	
	all_training_categories = TrainingCategory.objects.filter(
							trainingground=trainingground_obj
							).order_by('category')
	
	all_skill_list = []
	for training_category in all_training_categories:
		max_multi = training_category.maximum_multiplier
		skills = Skill.objects.filter(category=training_category.category)
		
		skill_list = []
		for skill in skills:
			if skill.multiplier <= max_multi:
				skill_list.append(skill)
				
		cat=[training_category.category.name, skill_list]
		all_skill_list.append(cat)
	
	
	return all_skill_list
		

#Gives a list of available skills to train at current location
def trainingground_get_character_skills(character_obj, trainingground_obj):
	"""
	list the available skills for the character in trianing grounds
	"""
	
	all_skill_list = trainingground_get_skills(trainingground_obj)
	
	all_possible_skills = []
	for category in all_skill_list:
		
		skill_list = []
		for skill in category[1]:
			try:
				char_skill_level = TrainedSkill.objects.get(
										character=character_obj,
										skill=skill
										).level
			except ObjectDoesNotExist:
				char_skill_level = 0
				
			max_train_level = trainingground_obj.level_upgrades + 1		
			
			if char_skill_level < max_train_level:
				skill_list.append(skill)
				
		cat = [category[0], skill_list]
		all_possible_skills.append(cat)
		
	return all_possible_skills
			
	

def trainingground_get_open_slots(trainingground_obj):
	"""
	get amount of open training slots in trainingground
	"""
	
	# Get maximum amount of characters in training at trainingground
	max_slots = trainingground_obj.current_characters
	count = SkillTrainingTimer.objects.filter(trainingground=trainingground_obj).count()
	
	return max_slots - count
