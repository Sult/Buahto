from django.contrib import admin
from characters.models import Character, FactionReputation, NpcGuildReputation



class CharacterAdmin(admin.ModelAdmin):
	fieldsets = [
		('General information', {'fields': ['name', 'user', 'faction', 'origin', 'safekeeping', 'bounty']}),
		('Portrait', {'fields': ['portrait'], 'classes': ['collapse']}),
	]
	
	list_display = ('name', 'user', 'creation', 'protected')
	list_filter = ['faction']
	search_fields = ('name', 'user')
	
	
class CharacterReputationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Faction Reputation', {'fields': ['character', 'faction', 'reputation']}),
	]
	
	list_display = ('character', 'faction', 'show_reputation')
	list_filter = ['faction']
	search_fields = ['character__name']
	

class NpcGuildReputationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Npc Guild Reputation', {'fields': ['character', 'npcguild', 'reputation']}),
	]
	
	list_display = ('character', 'npcguild', 'show_reputation')
	list_filter = ['npcguild']
	search_fields = ['character__name']
	
	
admin.site.register(Character, CharacterAdmin)
admin.site.register(FactionReputation, CharacterReputationAdmin)
admin.site.register(NpcGuildReputation, NpcGuildReputationAdmin)
