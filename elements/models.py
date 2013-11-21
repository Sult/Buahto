from django.db import models

from time import time
import datetime







#generalstats (like max characters, remap timers and more
class GeneralGameStats(models.Model):
	"""
	 time set game variables that (proberly) never change
	"""
	
	maximum_characters = models.IntegerField()
	character_protection = models.IntegerField()
	
	
	# Reputation likes dislikes
	is_faction = models.FloatField()
	likes_faction = models.FloatField()
	hates_faction = models.FloatField()
	
	
	
	def __unicode__(self):
		return "General Game statistics"



	


# the main factions
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



class FactionLike(models.Model):
	"""
	keep track fo relations between factions
	"""
	
	faction = models.ForeignKey(Faction, related_name='faction')
	likes_faction = models.ForeignKey(Faction, related_name='likes_faction')
	hates_faction = models.ForeignKey(Faction, related_name='hates_faction')
	
	def __unicode__(self):
		return "%s likes: %s, hates: %s" % (self.faction, 
									self.likes_faction, self.hates_faction)




#Faction Origins
class Origin(models.Model):
	"""
	Faction Origins for Characters.  determines equipment and skills
	"""
	faction = models.ForeignKey(Faction, editable=False)
	name =  models.CharField(max_length=32, unique=True)
	flavor = models.TextField(max_length=1024)
	
	
	# home region
	# starting skills + starting items
	
	def __unicode__(self):
		return self.name
		
		


class GuildCategory(models.Model):
	"""
	The different categories that give a general direction of guilds
	"""

	name = models.CharField(max_length = 31)
	
	def __unicode__(self):
		return self.name



# NPC Guils
class NpcGuild(models.Model):
	"""
	The NPC Guild related to factions, 
	"""
	
	faction = models.ForeignKey(Faction)
	category = models.ForeignKey(GuildCategory)
	
	name = models.CharField(max_length = 63)
	flavor = models.TextField(max_length = 1023)
	
	def __unicode__(self):
		return "%s - %s" % (self.name, self.faction)




#File upload name maker
def get_upload_file_name(instance, filename):
	return "uploaded_portraits/%s_%s" % (str(time()).replace('.','_'), filename)
	
# Portrait
class Portrait(models.Model):
	"""
	add immages for the portrait gallery
	"""
	
	name = models.CharField(max_length = 31, unique=True)
	portrait = models.FileField(upload_to=get_upload_file_name)
	
	def __unicode__(self):
		return self.name
