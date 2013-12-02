from django.contrib import admin
from towns.models import TrainingGround, TrainingCategory, Town


class TrainingCategoryInline(admin.TabularInline):	
	model = TrainingCategory
	extra = 1
	
	fieldsets = [
		('Training Skill Category', {'fields': ['trainingground', 'category', 'current_speed', 'maximum_speed', 'maximum_multiplier']}),
	]


class TrainingGroundAdmin(admin.ModelAdmin):
	fieldsets = [
		('Training Ground', {'fields': ['name', 'level_upgrades', 'multiplier_upgrades', 'current_characters', 'maximum_characters']}),
	]
	
	inlines = [TrainingCategoryInline]
	
	list_display = ('name', 'level_upgrades', 'multiplier_upgrades', 'current_characters', 'maximum_characters')



class TownAdmin(admin.ModelAdmin):
	fieldsets = [
		('Town Information', {'fields': ['name', 'flavor', 'faction']}),
		('Town Locations', {'fields': ['trainingground']})
		
	]

	list_display = ('name', 'faction')

admin.site.register(TrainingGround, TrainingGroundAdmin)


admin.site.register(Town, TownAdmin)
