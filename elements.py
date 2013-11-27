### Little script to load basic data into database after the need to rebuild it.

from elements.models import GameRelatedNumbers
from elements.models import Portrait, Attribute, Faction, FactionLike
from elements.models import SkillCategory, Skill



# Add general game stats
def add_gamerelatednumbers():
	gamerelated = GameRelatedNumbers(
		#character statistics
		character_protection = 14,
		maximum_characters = 3,
		
		
		#Attributes
		attribute_default = 20, 
		attribute_minimum = 15,
		attribute_maximum = 27,
		remap_timer = 60,
		remap_bonus = 1,
		
		# skills
		#basic_skill_points = 150,
		#default_multiplier = 2.3,
		#primary_multiplier = 1.2,
		#secundary_multiplier = 0.6,
		
		#Reputation statistics
		faction_is = 1000,
		faction_likes = 250,
		faction_hates = -500,
	)
		
	gamerelated.save()



# add the character portraits
def add_portraits():
	
	allportraits = (
		('Ajantis', '/home/ikke/panda/realbuahto/media/ajantis.jpg'),
		('Alora', '/home/ikke/panda/realbuahto/media/alora.jpg'),
		('Branwen', '/home/ikke/panda/realbuahto/media/branwen.jpg'),
		('Coran', '/home/ikke/panda/realbuahto/media/coran.jpg'),
		('Dynaheir', '/home/ikke/panda/realbuahto/media/dynaheir.jpg'),
		('Edwin', '/home/ikke/panda/realbuahto/media/edwin.jpg'),
		('Eldoth', '/home/ikke/panda/realbuahto/media/eldoth.jpg'),
		('Faldorn', '/home/ikke/panda/realbuahto/media/faldorn.jpg'),
		('Garrick', '/home/ikke/panda/realbuahto/media/garrick.jpg'),
		('Imoen', '/home/ikke/panda/realbuahto/media/imoen.jpg'),
	)
	
	for port in allportraits:
		
		new_port = Portrait(
			name = port[0],
			portrait = port[1],	
		)
		
		new_port.save()



# Add the main NPC Factions
def add_factions():
	#Input
	allfactions = (
		('Aramore', 'Flavortext'),
		('Harmstead', 'Flavortext'),
		('Solaris', 'Flavortext'),
		('Warnwick', 'Flavortext'),
	)
	
	for faction in allfactions:
		new_faction = Faction(
			name = faction[0],
			flavor = faction[1],
		)
	
		new_faction.save()



# Add faction likings towards each other
def add_faction_likes():
	faction_standings = (
		('Aramore', 'Harmstead', 'Solaris'),
		('Solaris', 'Warnwick', 'Aramore'),
		('Harmstead', 'Aramore', 'Warnwick'),
		('Warnwick', 'Solaris', 'Harmstead'),
	)
	
	for fact_standing in faction_standings:
		the_faction = Faction.objects.get(name=fact_standing[0])
		faction_likes = Faction.objects.get(name=fact_standing[1])
		faction_hates = Faction.objects.get(name=fact_standing[2])
		
		likes = FactionLike(
			faction = the_faction,
			likes_faction = faction_likes,
			hates_faction = faction_hates,
		)
		
		likes.save()


def add_attributes():
	allattributes = (
		('Strength'),
		('Dexterity'),
		('Constitution'),
		('Intelligence'),
		('Charisma'),
	)
	
	for attribute in allattributes:
		new_attribute = Attribute(
			name = attribute,
		)
		new_attribute.save()


def add_skillcategories():
	all_categories = (
		('Archery', 'flavor text'),
		('Armor', 'flavor text'),
		('Crafting', 'flavor text'),
		('Elixers', 'flavor text'),
		('Endurance', 'flavor text'),
		('Exploration', 'flavor text'),
		('Guild Management', 'flavor text'),
		('Leadership', 'flavor text'),
		('Mercenaries', 'flavor text'),
		('Navigation', 'flavor text'),
		('Resource Processing', 'flavor text'),
		('Science', 'flavor text'),
		('Social', 'flavor text'),
		('Town management', 'flavor text'),
		('Trade', 'flavor text'),
		('Travel', 'flavor text'),
		('Weapons', 'flavor text'),
	)
	
	for category in all_categories:
		new_category = SkillCategory(
							name=category[0],
							flavor=category[1],
		)
		new_category.save()
		


def add_some_skills():
	some_skills = (
		('Archery', 'Small Ranged Weapons', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Power Shot', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Fast Reload', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Precise Shot', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Medium Ranged Weapons', 'Dexterity', 'Strength', 'Flavor', 2),
		('Archery', 'Ambush', 'Dexterity', 'Strength', 'Flavor', 2),
		('Archery', 'Quick Draw', 'Dexterity', 'Strength', 'Flavor', 2),
	)
	
	for a_skill in some_skills:
		the_skill = Skill(
			name = a_skill[1],
			category = SkillCategory.objects.get(name=a_skill[0]),
			primary = Attribute.objects.get(name=a_skill[2]),
			secundary = Attribute.objects.get(name=a_skill[3]),
			flavor = a_skill[4],
			multiplier = a_skill[5],
		)
		the_skill.save()
		
		

add_gamerelatednumbers()
add_attributes()
add_portraits()
add_factions()
add_faction_likes()
add_skillcategories()
add_some_skills()
