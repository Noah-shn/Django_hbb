from django.urls import path
from . import views
from .views import test

urlpatterns = [

    path('test/', views.test, name='test'), 

    ]
