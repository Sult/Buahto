# The towns and their elements

from django.db import models

from elements.models import SkillCategory, Faction



### Town locations

# Traininggrounds Where players hone their skills
class TrainingGround(models.Model):
	"""
	The place where characters go to to set their skills int rianing, also holds space for posisble upgrades
	"""
	
	VERRY_LOW = 10
	LOW = 25
	NORMAL = 50 
	HIGH = 100
	VERRY_HIGH = 200
	MAX_CHAR = (
		(VERRY_LOW, 'Verry Low'),
		(LOW, 'Low'),
		(NORMAL, 'Normal'),
		(HIGH, 'High'),
		(VERRY_HIGH, 'Verry High'),
	)
	
	name = models.CharField(max_length=63)
	level_upgrades = models.IntegerField(default=0)
	multiplier_upgrades = models.IntegerField(default=0)
	current_characters = models.IntegerField(choices=MAX_CHAR)
	maximum_characters = models.IntegerField(choices=MAX_CHAR)
	
	def __unicode__(self):
		return self.name
	



#Trianinggrounds subclass
class TrainingCategory(models.Model):
	"""
	the available skills for the traininggrounds and the max posisble multiplyer of that specific category
	"""
	
	VERRY_SLOW = 0.8
	SLOW = 0.9
	NORMAL = 1
	FAST = 1.1
	VERRY_FAST = 1.2
	SPEED = (
		(VERRY_SLOW, 'Verry Slow'),
		(SLOW, 'Slow'),
		(NORMAL, 'Normal'),
		(FAST, 'Fast'),
		(VERRY_FAST, 'Verry Fast'),
	)
	
	trainingground = models.ForeignKey(TrainingGround)
	category = models.ForeignKey(SkillCategory)
	
	current_speed = models.FloatField(choices=SPEED)
	maximum_speed = models.FloatField(choices=SPEED)
	maximum_multiplier = models.IntegerField()
	
	def __unicode__(self):
		return self.category.name





#Town class that binds all together
class Town(models.Model):
	"""
	A town with their coordinates trianinggrounds quest office and all other relevant attributes
	"""
	
	# general town information
	name = models.CharField(max_length = 63)
	flavor = models.TextField(max_length = 511)
	faction = models.ForeignKey(Faction, blank=True)
	
	# location
	# x-y grid
	
	trainingground = models.ForeignKey(TrainingGround, blank=True)
	
	
	def __unicode__(self):
		return self.name
	
	
	
