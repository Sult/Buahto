#at the >>> prompt type the following:
#execfile("samples.py")

#Put in some data into databe to work with and test
#



from django.contrib.auth.models import User
from characters.models import Character, CharacterAttribute
from elements.models import GameRelatedNumbers, Timer, Skill
from elements.models import Portrait, Attribute, Faction, FactionLike, SkillCategory
from towns.models import TrainingGround, TrainingCategory, Town

from game_methods import character_logic

import datetime, time
from django.utils.timezone import utc




def add_some_towns():
	some_towns = (
		#('Name', 'Flavor', faction_id, trainingground_id)
		('Bari', 'Kinky Town', 1, 1),
		('Sultz', 'Deepthroaters', 2, 2),
		('Bonako', 'Bananas', 3, 3),
		('Neder', 'Pot Skunk Weed', 4, 4),
	)
	
	for town in some_towns:
		new_town = Town(
					name = town[0],
					flavor = town[1],
					faction = Faction.objects.get(id=town[2]),
					trainingground = TrainingGround.objects.get(id=town[3]),
		)
		new_town.save()


def add_timers():
	some_timers = (
		(0, 0, 1),
		(0, 0, 5),
		(0, 0, 10),
		(0, 0, 15),
		(0, 0, 30),
		(0, 0, 45),
		(0, 1, 0),
		(0, 1, 30),
		(0, 3, 0),
		(0, 6, 0),
		(0, 12, 0),
		(1, 0, 0),
		(3, 0, 0),
		(7, 0, 0),
	)
	for timer in some_timers:
		new_timer = Timer(
			days = timer[0],
			hours = timer[1],
			minutes = timer[2],
		)
		new_timer.save()

	

def add_users():
	some_users = (
		('Hoer', 'ikke@hier.daar', '1234'),
		('Pik', 'ikke@hier.daar', '1234'),
		('Zuigslet', 'ikke@hier.daar', '1234'),
		('Trut', 'ikke@hier.daar', '1234'),
		('Anaal', 'ikke@hier.daar', '1234'),
		('Slorie', 'ikke@hier.daar', '1234'),
		('Pastoortje', 'ikke@hier.daar', '1234'),
		('Zaadzuiger', 'ikke@hier.daar', '1234'),
		('Snol', 'ikke@hier.daar', '1234'),
	)
	
	
	for user in some_users:
		new_user = User.objects.create_user(user[0], user[1], user[2])
		
		print "%s" % new_user.username





def add_characters():
	some_characters = (
		#(useR_id, 'name', portrait_id, faction_id, town_id)
		(1,'Banaan', 2, 1, 1),
		(2,'Peer', 3, 2, 2),
		(2,'Appel', 5, 3, 3),
		(3,'Mandarijn', 1, 4, 4),
		(3,'Passievrucht', 6, 1, 1),
		(3,'Meloen', 2, 3, 2),
		(4,'Pruim', 1, 3, 3),
		(5,'Perzik', 7, 4, 4),
		(6,'Aardbei', 2, 3, 1),
		(7,'Sinasappel', 2, 2, 2),
		(8,'Bes', 1, 3, 3),
		(8,'Framboos', 1, 4, 4),
	)
	
	
	for new_char in some_characters:
		
		character = Character(
						user = User.objects.get(id=new_char[0]),
						name = new_char[1],
						portrait = Portrait.objects.get(id=new_char[2]),
						faction = Faction.objects.get(id=new_char[3]),
						remap = datetime.datetime.now(),
						bonus_remaps = 2,
						town = Town.objects.get(id=new_char[4]),
					)
		character.save()
		
		#add subtables
		character_logic.create_character(character)
		
		print character.name
		


#### Town elements ####
#Add some training ground examples
def add_trainingground():
	some_tg = (
		#('name', maximum_upgrades, maximum_characters)
		('Basic Training Ground'), 
		('Standard Training Ground'),
		('Advanced Training Ground'),
		('Expert Training Ground'),
		
		('Archery Training Ground'),
		('Expert Archery Training Ground'),
	)
	
	for tg in some_tg:
		new_tg = TrainingGround(
			name = tg,
			level_upgrades = 0,
			current_characters = 25,
			maximum_characters = 100,
			multiplier_upgrades = 0,
		)
		new_tg.save()
	
	
	




def add_some_skills():
	some_skills = (
		('Archery', 'Small Ranged Weapons', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Power Shot', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Fast Reload', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Precise Shot', 'Dexterity', 'Strength', 'Flavor', 1),
		('Archery', 'Medium Ranged Weapons', 'Dexterity', 'Strength', 'Flavor', 2),
		('Archery', 'Ambush', 'Dexterity', 'Strength', 'Flavor', 2),
		('Archery', 'Quick Draw', 'Dexterity', 'Strength', 'Flavor', 2),
		
		('Skirmish', 'Small Melee Weapons', 'Strength', 'Constitution', 'Flavor', 1),
		('Skirmish', 'Power Strike', 'Strength', 'Constitution', 'Flavor', 1),
		('Skirmish', 'Fast Punch', 'Strength', 'Dexterity', 'Flavor', 1),
		('Skirmish', 'Piercing Strike', 'Strength', 'Dexterity', 'Flavor', 1),
		('Skirmish', 'Medium Melee Weapons', 'Strength', 'Constitution', 'Flavor', 2),
		('Skirmish', 'Furious Hit', 'Strength', 'Constitution', 'Flavor', 2),
		('Skirmish', 'Rapid Strike', 'Strength', 'Dexterity', 'Flavor', 2),
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
		


		
		
		

#add_users()
add_trainingground()
add_some_towns()

add_characters()
add_timers()

add_some_skills()

# Town elements



