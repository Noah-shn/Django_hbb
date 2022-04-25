from django.urls import path
from . import views
from .views import (
    sellcategorie,
    about,
	PostListView, 
	PostDetailView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'), 
    path('sellcategorie/', views.sellcategorie, name='blog-sellcategorie'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-detail'),
    ]
