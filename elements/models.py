from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from time import time
import datetime
from django.utils.timezone import utc


#### GAME RELATED NUMBERS ####

# used to store 1 time only data about math and other game related functions
class GameRelatedNumbers(models.Model):
	"""
	A list of one row only data about game mechanics and variables of mathematical functions
	"""
	
	# About Characters
	character_protection = models.IntegerField()			# Duration of character protection in days
	maximum_characters = models.IntegerField()				# Maximum amount of characters a user may have
	
	#attributes
	attribute_default = models.IntegerField()				# Default attribute score
	attribute_minimum = models.IntegerField()				# Minimum allowed attribute score
	attribute_maximum = models.IntegerField()				# Maximum allowed attribute score
	remap_timer = models.IntegerField()						# Timer on attribute remapping in days
	remap_bonus = models.IntegerField() 					# bonus remaps before you get a timer
	
	#Skills
	secundary_bonus = models.FloatField()					# multiplier  of secundary attribute that helps shorten training time
	base_skill_points = models.IntegerField()				# amount of basic points needed for math
	base_power_of = models.FloatField()						# Number to be the power of 
	power_of_multiplier = models.FloatField()				# power of increasement for higher multiplier skills
	
	# Reputations
	faction_is = models.IntegerField()						# Reputation on character faction on creation
	faction_likes = models.IntegerField()					# Reputation on friend faction on creation
	faction_hates = models.IntegerField()					# Reputation on enemy faction on creation



class TownRelatedNumbers(models.Model):
	"""
	Holds the varaibles related to town management
	"""
	
	#overal town related
	max_char_in_town = models.IntegerField()				# max online people in 1 town
	max_upgrades = models.IntegerField()					# max "town" upgrades 
	
	
	# Trainingground related
	max_trainingground_upgrades = models.IntegerField()		# max "trainingground" upgrades
	max_char_in_training = models.IntegerField()			# max characters in trianing at trainingground
	
	


class Timer(models.Model):
	"""
	Set of timers that cna be used for different activities throughout the game
	Keep in mind timers can be reduced by skills or other options
	"""
	
	minutes = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
	hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
	days = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
	
	def __unicode__(self):
		return "Minutes: %s Hours: %s Days: %s" % (self.minutes, self.hours, self.days)
	
	
	
	
	


#### CHARACTER ELEMENTS ####

#File upload name maker
def get_upload_file_name(instance, filename):
	return "uploaded_portraits/%s_%s" % (str(time()).replace('.','_'), filename)
	

# Character Portraits
class Portrait(models.Model):
	"""
	add immages for the portrait gallery
	"""
	
	name = models.CharField(max_length = 31, unique=True)
	portrait = models.FileField(upload_to=get_upload_file_name)
	
	def __unicode__(self):
		return self.name
		

	
		
# Different Character Attributes
class Attribute(models.Model):
	"""
	The different attributes of a character
	"""

	name = models.CharField(max_length = 15, unique=True)
	
	def __unicode__(self):
		return self.name


#The skills
class SkillCategory(models.Model):
	"""
	different skill categories
	"""

	name = models.CharField(max_length=31, unique=True)
	flavor = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name		


class Skill(models.Model):
	"""
	Skill template for every skill
	"""
	
	primary = models.ForeignKey(Attribute, related_name='primary')
	secundary = models.ForeignKey(Attribute, related_name='secundary')
	category = models.ForeignKey(SkillCategory)
	
	name = models.CharField(max_length=63)
	flavor = models.TextField(max_length=255)
	multiplier = models.IntegerField()
	
	def __unicode__(self):
		return self.name
	



# the main NPC Factions
class Faction(models.Model):
	"""
	Main factions in Buahto, chatacters choose one of these at start
	"""

	name =  models.CharField(max_length=32, unique=True)
	flavor = models.TextField(max_length=1024)
		
	# Add important people / story?
	# home region
	# More
	
	def __unicode__(self):
		return self.name
		


	
# Reputations between factions
class FactionLike(models.Model):
	"""
	keep track fo relations between factions
	"""
	
	faction = models.ForeignKey(Faction, unique=True, related_name='faction')
	likes_faction = models.ForeignKey(Faction, related_name='likes_faction')
	hates_faction = models.ForeignKey(Faction, related_name='hates_faction')
	
	def __unicode__(self):
		return "%s likes: %s, hates: %s" % (self.faction, 
									self.likes_faction, self.hates_faction)



	
