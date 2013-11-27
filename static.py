#at the >>> prompt type the following:
#execfile("script.py")

"""
Little script to load basic data into database after the need to rebuild it.
"""

from elements.models import Faction, FactionLike, Origin, GuildCategory
from elements.models import Portrait
from elements.models import GeneralGameStats, Attribute, SkillCategory





# Main Factions
# Add Factions, origins
def add_factions():
	#Input
	allfactions = [
		'Aramore---Flavortext',
		'Harmstead---Flavortext',
		'Solaris---Flavortext',
		'Warnwick---Flavortext',
	]
	
	for faction in allfactions:
		
		new = faction.split('---')
				
		new_faction = Faction(
			name = new[0],
			flavor = new[1],
		)
	
		new_faction.save()


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
	
def add_origins():
	allorigins = (
		('Therino', 1, 'Flavortext'),
		('Merri', 1, 'Flavortext'),
		('Belwyn', 1, 'Flavortext'),
		('Risbel', 1, 'Flavortext'),
		('Lealom', 2, 'Flavortext'),
		('Vesemm', 2,'Flavortext'),
		('larangha', 2, 'Flavortext'),
		('Hedgeki', 2, 'Flavortext'),
		('Tainy', 3, 'Flavortext'),
		('Poln', 3, 'Flavortext'),
		('Etys', 3, 'Flavortext'),
		('Torpol', 3, 'Flavortext'),
		('Leraldo', 4, 'Flavortext'),
		('Bany', 4, 'Flavortext'),
		('Isaen', 4, 'Flavortext'),
		('Igaro', 4, 'Flavortext'),
	)
		
	for origin in allorigins:
		
		faction = Faction.objects.get(id=origin[1])
		
		new_origin = Origin(
			faction = faction,
			name = origin[0],
			flavor = origin[2]
		)
	
		new_origin.save()


# Add general game stats
def add_generalgamestats():
	generalstats = GeneralGameStats(
		#character statistics
		maximum_characters = 3,
		character_protection = 14,
		default_attribute = 20, 
		minimum_attribute = 15,
		maximum_attribute = 27,
		
		# skills
		basic_skill_points = 150,
		default_multiplier = 2.3,
		primary_multiplier = 1.2,
		secundary_multiplier = 0.6,
		
		#Reputation statistics
		is_faction = 1.000,
		likes_faction = 0.250,
		hates_faction = -0.500,
		)
		
	generalstats.save()

def add_attributes():
	allattributes = (
		('Strength'),
		('Constitution'),
		('Dexterity'),
		('Intelligence'),
		('Wisdom'),
		('Charisma'),
	)
	
	for attribute in allattributes:
		new_attribute = Attribute(
			name = attribute,
		)
		new_attribute.save()


#def add_portraits():
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
			portrait = port[1]
			
		)
		
	
		new_port.save()


# Add all guild categories
def add_guildcategories():
	
	allcategories = [
		'Combat',
		'Logistics',
		'Industry',
		'Warfare',
		]
		
	for cate in allcategories:
		
		new_category = GuildCategory(name=cate)
		new_category.save()
				

def add_skillcategories():
	all_categories = (
		('Archery', 'flavor text'),
		('Armor', 'flavor text'),
		('Elixers', 'flavor text'),
		('Endurance', 'flavor text'),
		('Exploration', 'flavor text'),
		('Guild Management', 'flavor text'),
		('Mercenaries', 'flavor text'),
		('Navigation', 'flavor text'),
		('Production', 'flavor text'),
		('Resource Processing', 'flavor text'),
		('Science', 'flavor text'),
		('Social', 'flavor text'),
		('Tactics', 'flavor text'),
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



add_factions()
add_faction_likes()
add_origins()
add_generalgamestats()
add_attributes()
add_guildcategories()
add_portraits()
add_skillcategories()

