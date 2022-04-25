from django import forms
from django.forms import ModelForm
from .models import produit

class produitForm(ModelForm):
	class Meta:
		model = produit
		fields =['choix','serie']

class SearchForm(forms.Form):
    type = forms.ChoiceField(choices = ((1, 'One'), (2, 'Two')))

    # Use any form fields you need, CharField for simplicity reasons
    list1 = forms.CharField()
    list2 = forms.CharField()
#form that update the profile