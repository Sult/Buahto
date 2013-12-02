# File ment to help out on game logic and database handeling
# mathematical logic to calculate game elements

#TODO: Make error log if things go wrong


import datetime
import time
from django.utils.timezone import utc

from django.core.exceptions import ObjectDoesNotExist
from game_methods import town_logic

from elements.models import GameRelatedNumbers, Attribute, Faction, FactionLike
from characters.models import Character, CharacterAttribute, FactionReputation
from characters.models import TrainedSkill, SkillTrainingTimer
from towns.models import TrainingCategory




#Create a new Character
def create_character(character_obj):
	"""
	Add all the subtables needed to "save" a complete character
	"""
		
	# Create Character Attributes Table
	attributes = Attribute.objects.all()
	for attribute in attributes:
		new_attribute = CharacterAttribute(
			character = character_obj,
			attribute = attribute,
			score = GameRelatedNumbers.objects.get(id=1).attribute_default,
		)
		new_attribute.save()


	#Create factions for character
	get_factions = Faction.objects.all()
	get_likes = FactionLike.objects.get(faction=character_obj.faction)
	
	for fact in get_factions:
		if fact == get_likes.faction:
			reputation = GameRelatedNumbers.objects.get(id=1).faction_is
		elif fact == get_likes.likes_faction:
			reputation = GameRelatedNumbers.objects.get(id=1).faction_likes
		elif fact == get_likes.hates_faction:
			reputation = GameRelatedNumbers.objects.get(id=1).faction_hates
		else:
			reputation = 0.000
		
		add_faction = FactionReputation(
			character = character_obj,
			faction = fact,
			reputation=reputation
		)
		add_faction.save()


#set a new remap timer
def set_remap_timer(character_obj):
	get_timer = GameRelatedNumbers.objects.get(id=1).remap_timer
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	new_date = now + datetime.timedelta(days=get_timer)
	character_obj.remap = new_date
	character_obj.save()





# add reputation to faction
def add_reputation(character_obj, faction_obj, amount):
	"""
	Add a reputation to a faction.
	Amount should be a percentage 
	"""
	try:
		reputation_obj = FactionReputation.objects.get(character=character_obj, faction = faction_obj)
	except ObjectDoesNotExist:
		new_reputation = FactionReputation(
							character=character_obj, 
							faction=faction_obj, 
							reputation=0
						)
		new_reputation.save()
			
	
	if amount < 0:
		new_reputation = ((-100 - reputation_obj.reputation) * amount) + reputation_obj.reputation
	elif amount >= 0:
		new_reputation = ((-100 - reputation_obj.reputation) * amount) + reputation_obj.reputation
	else:
		#Make some error log that something is going wrong
		pass
		

def train_skill(character_obj, skill_obj):
	"""
	check if trainingground has still training spots open.
	check if character has skill already, and if not, add it
	"""
	
	error = False
	
	# Get open slots
	open_slots = town_logic.trainingground_get_open_slots(character_obj.town.trainingground)
	
	if open_slots < 1:
		error = "No available training spots left."
		
	else:
		
		# get character trianing timer
		try:
			skill_training = SkillTrainingTimer.objects.get(character=character_obj)
		except ObjectDoesNotExist:
			skill_training = SkillTrainingTimer(
							character=character_obj,
							skill = skill_obj,
							trainingground = character_obj.town.trainingground,
							timer = datetime.datetime.utcnow().replace(tzinfo=utc),
			)
	
		if datetime.datetime.utcnow().replace(tzinfo=utc) < skill_training.timer:
			error = "You are already training a skill"
		else:
			# Skill training possible
		
			#Get (or add) trained_skill object
			try:
				char_skill = TrainedSkill.objects.get(character=character_obj, skill=skill_obj)
			except ObjectDoesNotExist:
				char_skill = TrainedSkill(
						character=character_obj,
						skill=skill_obj,
				)
				char_skill.save()
		
			# set timer
			skill_training.skill = skill_obj
			skill_training.trainingground = character_obj.town.trainingground
			skill_training.timer = datetime.datetime.utcnow().replace(tzinfo=utc) + get_skill_training_time(character_obj, skill_obj)
			skill_training.save()
			print skill_training
	return skill_training.timer, error
			
	
	
	

# get the trainingtime of 
def get_skill_training_time(character_obj, skill_obj):
	"""
	get the time it takes to train a skill based on level attributes and skill difficulty
	"""
	
	try:
		char_skill = TrainedSkill.objects.get(character=character_obj, skill=skill_obj).level
	except ObjectDoesNotExist: 
		char_skill = 0
	
	#Get trainingground speed modifier
	train_speed = TrainingCategory.objects.get(
									trainingground = character_obj.town.trainingground,
									category = skill_obj.category
									).current_speed
	
	# Get the attributes and equation numbers
	primary_att = CharacterAttribute.objects.get(
							character=character_obj,
							attribute=skill_obj.primary
							).score
	secundary_att = CharacterAttribute.objects.get(
							character=character_obj, 
							attribute=skill_obj.secundary
							).score
	number = GameRelatedNumbers.objects.get(id=1)
	
	#calculate trainspeed
	points_per_second = (primary_att + secundary_att * number.secundary_bonus) / 60 * train_speed
	
	# Calculate points needed
	points_multiplier = number.base_power_of ** ((number.power_of_multiplier * char_skill) - number.power_of_multiplier)
	points_needed = points_multiplier * number.base_skill_points * skill_obj.multiplier
	
	#training time in datetime format
	training_time = datetime.timedelta(seconds=int(points_needed/points_per_second))
	return training_time
