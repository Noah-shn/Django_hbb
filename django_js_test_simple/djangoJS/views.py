from django.shortcuts import render
from .models import produit
from .form import produitForm


# Create your views here.

def test(request):
	form = produitForm(request.POST)
	return render(request,'djangoJS/test.html',{'form':form})