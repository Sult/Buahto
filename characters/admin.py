from django.contrib import admin
from characters.models import Character, CharacterAttribute
from characters.models import FactionReputation, TrainedSkill


# Character information
class CharacterAdmin(admin.ModelAdmin):
	fieldsets = [
		('General information', {'fields': ['name', 'user', 'faction']}),
		('Portrait', {'fields': ['portrait', 'remap'], 'classes': ['collapse']}),
	]
	
	list_display = ('name', 'user', 'protected')
	list_filter = ['faction']
	search_fields = ('name', 'user')
	
	
#Character attributes (want to inline collapsed later)
class CharacterAttributeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Character Attributes', {'fields': ['character', 'attribute', 'score']}),
	]
	
	list_display = ('attribute', 'score', 'character')
	list_filter = ['attribute']
	search_fields = ['character__name']


#Character Faction overview	
class FactionReputationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Faction Reputation', {'fields': ['character', 'faction', 'reputation']}),
	]
	
	list_display = ('character', 'faction', 'show_reputation')
	list_filter = ['faction']
	search_fields = ['character__name']
	
class TrainedSkillAdmin(admin.ModelAdmin):
	fieldsets = [
		('Skill', {'fields': ['skill', 'level', 'character']}),
	]
	
	list_display = ('skill', 'level', 'character')
	list_filter = ['level']
	search_fields = ('skill__name', 'character__name')
	
	


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterAttribute, CharacterAttributeAdmin)
admin.site.register(FactionReputation, FactionReputationAdmin)
admin.site.register(TrainedSkill, TrainedSkillAdmin)
