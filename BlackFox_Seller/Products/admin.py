from django.contrib import admin
from .models import Monitors, GraphicImage,GraphicCards,Sell

# Register your models here.

admin.site.register(GraphicCards)
admin.site.register(Monitors)
admin.site.register(Sell)