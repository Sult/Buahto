from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from elements.models import GameRelatedNumbers
from elements.models import Portrait, Attribute, Faction, FactionLike, Skill

import time
import datetime



# Topllayer of a character
# links it to user and gives basic information
class Character(models.Model):
	"""
	Players character and the related attributes
	"""
	
	
	user = models.ForeignKey(User)
	
	creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
	name = models.CharField(max_length=32, unique=True)									# make title
	portrait = models.ForeignKey(Portrait)
	faction = models.ForeignKey(Faction) 
	# guild = models.ForeignKey(Guild)
	
	remap = models.DateTimeField(blank=True)
	bonus_remaps = models.IntegerField()

	
	def remap_available(self):
		return self.remap < timezone.now()

	
	# New player protection (set to 14 days)
	def protected(self):
		safe_days = GameRelatedNumbers.objects.get(id=1).character_protection
		return self.creation >= timezone.now() - datetime.timedelta(days=safe_days)
    
	protected.admin_order_field = 'creation'
	protected.boolean = True
	protected.short_description = 'Protected'
	
	
	def __unicode__(self):
		return self.name
		



#Basic stats that determine how fast a character can train skills
class CharacterAttribute(models.Model):
	"""
	Give a character score to all different attributes and get a remap timer
	"""
	
	character = models.ForeignKey(Character)
	attribute = models.ForeignKey(Attribute)
	score = models.IntegerField()
	
	
	def __unicode__(self):
		return "%s: %s" % (self.attribute, self.score)
		



# Reputation towards the different factions
class FactionReputation(models.Model):
	"""
	Character faction reputations
	"""
	
	character = models.ForeignKey(Character)
	faction = models.ForeignKey(Faction)
	reputation = models.IntegerField()
	
	

	## Show reputation on site 	
	def show_reputation(self):
		rep = ((self.reputation/100)+0.0)/10
		return rep
	
	show_reputation.admin_order_field = "faction"
	show_reputation.short_description = "Reputation"
	
	
	def __unicode__(self):
		return self.faction.name
	


# The trained character skills. 
class TrainedSkill(models.Model):
	"""
	All the trained skills of a character and their current level
	"""
	
	character = models.ForeignKey(Character)
	skill = models.ForeignKey(Skill)
	
	level = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.skill
	
