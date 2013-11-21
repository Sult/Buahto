# create the lists for globals,

#TODO: make functions to edit these lists from shell or other place


# Attributes	
def attributes():
	"""
	The attributes and their defautl scores + limits
	"""
	
	global allattributes
	
	allattributes = [
		'Strength',
		'Constitution',
		'Dexterity',
		'Intelligence',
		'Wisdom',
		'Charisma'
	]

	default_score = 20
	minimum_score = 15
	maximum_score = 25

		
# Guild Categories
def guild_categories():
	"""
	Guild categories and other general information about guilds
	"""
	global allcategories
	allcategories = [
		'Combat',
		'Logistics',
		'Industry',
		'Warfare'
		]



# Add Skill Categories
def add_skillcategories():
	"""
	All different skillcategories and other general information about skills
	"""
	
	global allskillcategories
	allskillcategories = [
		'Archery',
		'Armor',
		'Boosters',
		'Endurance',
		'Exploration',
		'Guild Management',
		'Navigation',
		'Production',
		'Resource Processing',
		'Knowledge',
		'Social',
		'Squires',
		'Tactical',
		'Town management',
		'Trade',
		'Travel',
		'Weapons'
	]
	

