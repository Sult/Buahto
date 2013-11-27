# File ment to help out on game logic and database handeling
# mathematical logic to calculate game elements

#TODO: Make error log if things go wrong


import datetime
import time

from elements.models import GameRelatedNumbers, Attribute, Faction, FactionLike
from characters.models import Character, CharacterAttribute, FactionReputation


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
	new_date = timezone.now() + datetime.timedelta(days=get_timer)
	character_obj.remap = new_date
	character_obj.save()



# add reputation to faction
def add_reputation(character_obj, faction_obj, amount):
	"""
	Add a reputation to a faction.
	Amount should be a percentage 
	"""
	
	reputation_obj = FactionReputation.objects.get(character=character_obj, faction = faction_obj)
	
	if amount < 0:
		new_reputation = ((-100 - reputation_obj.reputation) * amount) + reputation_obj.reputation
	elif amount > 0:
		new_reputation = ((-100 - reputation_obj.reputation) * amount) + reputation_obj.reputation
	else:
		#Make some error log that something is going wrong
		pass
		
	
	



