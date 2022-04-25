from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from .forms import SellForm
from django.views.generic import (
									ListView, 
									DetailView, 
									CreateView,
									UpdateView,
									DeleteView)
from .models import GraphicCards, Monitors, Sell


def sellcategorie(request):

	return render(request,'blog/sellcategorie.html')


def Sell_page(request):

	form = SellForm(request.POST)
	
	return render(request, 'Products/Sell.html',{'form':form})


class GraphicCardsList(ListView): #<app>/<model>_<viewtype>.html
	model = GraphicCards
	ordering =['-date_posted']


class GraphicDetail(DetailView):
	model = GraphicCards

class GraphicCreateView(LoginRequiredMixin, CreateView):
	model = GraphicCards
	fields = ['brand', 'title', 'description', 'price','image']


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		GraphicCards = self.get_object()
		if self.request.user == GraphicCards.author:
			return True
		return False

class GraphicUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = GraphicCards
	fields = ['brand', 'title', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		GraphicCards = self.get_object()
		if self.request.user == GraphicCards.author:
			return True
		return False

class GraphicDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = GraphicCards
	success_url = '/'

	def test_func(self):
		GraphicCards = self.get_object()
		if self.request.user == GraphicCards.author:
			return True
		return False

def cards(request):
		context = {
			'GraphicCards' : GraphicCards.objects.all()
		}
		return render(request, 'blog/graphic_cards.html', context)

def screens(request):
		context ={
			'monitors' : Monitors.objects.all()
		}
		return render(request, 'blog/monitors.html', context)

class MonitorsList(ListView): #<app>/<model>_<viewtype>.html
	model = Monitors
	ordering =['-date_posted']


class MonitorsDetail(DetailView):
	model = Monitors

class MonitorsCreateView(LoginRequiredMixin, CreateView):
	model = Monitors
	fields = ['brand', 'title', 'description','image']


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		Monitors = self.get_object()
		if self.request.user == Monitors.author:
			return True
		return False