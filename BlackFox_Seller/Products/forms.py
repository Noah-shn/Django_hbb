from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Sell

class SellForm(ModelForm):
	class Meta:
		model = Sell
		fields =['Product_name', 'Product_Type', 'description']

#form that update the profile
