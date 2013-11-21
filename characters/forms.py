from django import forms

from characters.models import Character

class CreateCharacterForm(forms.ModelForm):


	
	class Meta:
		model = Character
		
		fields = ['name', 'portrait', 'faction', 'origin']

