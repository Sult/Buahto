from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from time import time
import datetime

#implement app models
from elements.models import Faction, FactionLike, Origin, NpcGuild
from elements.models import GeneralGameStats, Portrait

# Top character class
class Character(models.Model):
	"""
	Players character and the related attributes
	"""
	
	
	user = models.ForeignKey(User)
	
	creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
	name = models.CharField(max_length=32, unique=True)
	portrait = models.ForeignKey(Portrait)
	faction = models.ForeignKey(Faction)
	origin = models.ForeignKey(Origin) 
	# guild = models.ForeignKey(Guild)
	# alliance = models.ForeignKey(Alliance)
	safekeeping = models.IntegerField(default=0)
	bounty = models.IntegerField(default=0)
	
	
	def __unicode__(self):
		return self.name
		
	
	# New player protection (set to 14 days)
	def protected(self):
		safe_days = GeneralGameStats.objects.get(id=1).character_protection
		return self.creation >= timezone.now() - datetime.timedelta(days=safe_days)
    
	protected.admin_order_field = 'creation'
	protected.boolean = True
	protected.short_description = 'Protected'
	
	
	#Create factions for character
	def create_factions(char_obj):
		get_factions = Faction.objects.all()
		get_likes = FactionLike.objects.get(faction=char_obj.faction)
		
		for fact in get_factions:
			if fact == get_likes.faction:
				reputation = GeneralGameStats.objects.get(id=1).is_faction
			elif fact == get_likes.likes_faction:
				reputation = GeneralGameStats.objects.get(id=1).likes_faction
			elif fact == get_likes.hates_faction:
				reputation = GeneralGameStats.objects.get(id=1).hates_faction
			else:
				reputation = 0.000
			
			add_faction = FactionReputation(
				character = char_obj,
				faction = fact,
				reputation=reputation
			)
			add_faction.save()
	
	
# Faction reputationf or characters
class FactionReputation(models.Model):
	"""
	Character faction reputations
	"""
	
	character = models.ForeignKey(Character)
	faction = models.ForeignKey(Faction)
	reputation = models.FloatField()
	
	
	
	# add reputation to faction
	def add_reputation(character_obj, faction_obj, amount):
		add_rep = FactionReputation.objects.get(character_obj, faction_obj)
		add_rep.reputation = add_rep.reputation + amount
		
		



	def __unicode__(self):
		return self.faction.name

	# Show reputation on site ( -2 decimals)	
	def show_reputation(self):
		rep = (int(self.reputation * 10)+0.0)/10
		return rep
	
	show_reputation.admin_order_field = "faction"
	show_reputation.short_description = "Reputation"
	
	
		


# npc 
class NpcGuildReputation(models.Model):
	"""
	character NPC Guild standings
	"""
	
	character = models.ForeignKey(Character)
	npcguild = models.ForeignKey(NpcGuild, unique=True)
	reputation = models.FloatField()
	
	def __unicode__(self):
		return self.npcguild.name
		
		
	# Show reputation on site ( -2 decimals)	
	def show_reputation(self):
		rep = (int(self.reputation * 10)+0.0)/10
		return rep
	
	show_reputation.admin_order_field = "npcguild"
	show_reputation.short_description = "Reputation"
	
	# check or create reputation and add value
	def add_reputation(character_obj, npcguild_obj, amount):
		if NpcGuildReputation.objects.get(character_obj, npcguild_obj):
			add_rep = NpcGuildReputation.objects.get(character_obj, npcguild_obj)
			add_rep.reputation = add_rep.reputation + amount
			add_rep.save()
		else:
			new_npcguild = NpcGuildReputation(
				character = character_obj,
				npcguild = npcguild_obj,
				reputation = amount,
			)
			new_npcguild.save()
	
				
				
