from django import forms

from characters.models import Character, CharacterAttribute

class CreateCharacterForm(forms.ModelForm):
	"""
	Form to create a new character
	"""

	class Meta:
		model = Character
		fields = ['name', 'portrait', 'faction']


class RemapForm(forms.ModelForm):
	"""
	Form used to do attribute remaps
	"""
	
	class Meta:
		model = CharacterAttribute
		fields = ['score']
