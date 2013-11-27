#at the >>> prompt type the following:
#execfile("samples.py")

#Put in some data into databe to work with and test
#



from django.contrib.auth.models import User
from characters.models import Character, CharacterAttribute
from elements.models import GameRelatedNumbers
from elements.models import Portrait, Attribute, Faction, FactionLike

from game_logic import character_logic

import datetime, time

	

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
		(1,'Banaan', 2, 1,),
		(2,'Peer', 3, 2),
		(2,'Appel', 5, 3),
		(3,'Mandarijn', 1, 4),
		(3,'Passievrucht', 6, 1),
		(3,'Meloen', 2, 3),
		(4,'Pruim', 1, 3,),
		(5,'Perzik', 7, 4,),
		(6,'Aardbei', 2, 3),
		(7,'Sinasappel', 2, 2),
		(8,'Bes', 1, 3),
		(8,'Framboos', 1, 4),
	)
	
	
	for new_char in some_characters:
		
		character = Character(
						user = User.objects.get(id=new_char[0]),
						name = new_char[1],
						portrait = Portrait.objects.get(id=new_char[2]),
						faction = Faction.objects.get(id=new_char[3]),
						remap = datetime.datetime.now(),
						bonus_remaps = 2,
					)
		character.save()
		
		#add subtables
		character_logic.create_character(character)
		
		print character.name
		






add_users()
add_characters()
