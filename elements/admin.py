from django.contrib import admin
from elements.models import Skill, Timer


class SkillAdmin(admin.ModelAdmin):
	fieldsets = [
		('Skill Information', {'fields': ['name', 'flavor']}),
		('Skill Data', {'fields': ['category', 'primary', 'secundary', 'multiplier'], 'classes': ['collapse']}),
	]
	
	list_display = ('name', 'category', 'primary', 'secundary', 'multiplier')
	list_filter = ('category', 'primary', 'multiplier')
	search_fields = ['name']



class TimerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Timer', {'fields': ['minutes', 'hours', 'days']}),
	]



admin.site.register(Skill, SkillAdmin)
admin.site.register(Timer, TimerAdmin)
