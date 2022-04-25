from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.views.generic import (
									ListView, 
									DetailView, 
									CreateView,
									UpdateView,
									DeleteView)
from .models import Post


def sellcategorie(request):

	return render(request,'blog/sellcategorie.html')


def home(request):
		context = {
			'posts' : Post.objects.all()
		}
		return render(request, 'blog/home.html',context)

def about(request):
		return render(request, 'blog/about.html',{'title': 'About'})

class PostListView(ListView):#<app>/<model>_<viewtype>.html
	model = Post
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

def screens(request):
		context ={
			'monitors' : Monitors.objects.all()
		}
		return render(request, 'blog/monitors.html', context)
