from django.contrib import admin
from elements.models import Faction, FactionLike, Origin
from elements.models import Portrait, GeneralGameStats


# General game settings
class GeneralGameStats(admin.ModelAdmin):
	fieldsets = [
		('General Game Settings', {'fields': ['maximum_characters'], 'classes': ['collape']}),
	]
	

# Make origin admin (inlines in Faction)
class OriginInline(admin.StackedInline):
	model = Origin
	extra = 0
	
	fieldsets = [
		('Faction', {'fields': ['name', 'flavor']}),
	]

#Faction admin
class FactionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Faction', {'fields': ['name', 'flavor']}),
	]
	
	inlines = [OriginInline]

#Faction standings with other factions
class FactionLikeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Faction Standings with others', {'fields': ['faction', 'likes_faction', 'hates_faction']}),
	]


class PortraitAdmin(admin.ModelAdmin):
	fieldsets = [
		('Portrait', {'fields': ['name', 'portrait']}),
	]

	list_display = ('name', 'portrait')
	search_fields = ['name']



admin.site.register(Faction, FactionAdmin)
admin.site.register(FactionLike, FactionLikeAdmin)
admin.site.register(Portrait, PortraitAdmin)
