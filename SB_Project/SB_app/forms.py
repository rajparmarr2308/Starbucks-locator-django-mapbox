# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Location

# create a ModelForm
class LocationForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Location
		fields = ['city']
