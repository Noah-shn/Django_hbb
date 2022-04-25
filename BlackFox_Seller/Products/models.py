from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class GraphicCards(models.Model):
	BrandChoice = (('Nvidia','Nvidia'),('AMD','AMD'), ('Intel','Intel'))
	brand = models.CharField(max_length=50, choices = BrandChoice, default='GrahicCard')
	title = models.CharField(max_length=35)
	description = models.TextField(max_length=200)
	price = models.IntegerField(default = 0)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	image=models.FileField(default='default.jpg', blank=True)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('graphic-cards-detail', kwargs={'pk' : self.pk})

class GraphicImage(models.Model):
	post = models.ForeignKey(GraphicCards, default=None, on_delete=models.CASCADE)
	images = models.FileField(upload_to ='graphiccards_pics')


class Monitors(models.Model):
	BrandChoice = (('BenQ','BenQ'),('MSI','MSI'), ('AOC','AOC'),('Asus','Asus'))
	brand = models.CharField(max_length=50, choices = BrandChoice, default='Monitors')
	title = models.CharField(max_length=20)
	description = models.TextField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg', upload_to='monitors_pics')
	date_posted = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('Monitors-detail', kwargs={'pk' : self.pk})


class Sell(models.Model):
    # Product Choices
    CHOICES = [
    ('Graphic Cards', (
            ('Nvidia', 'Nvidia'),
            ('AMD', 'AMD'),
        )
    ),
    ('Monitors', (
            ('BenQ', 'BenQ'),
            ('MSI', 'MSI'),
        )
    ),
    ]
    CHOICES_CARD = [
    ('Nvidia', (
            ('RTX', 'RTX'),
            ('GTX', 'GTX'),
        )
    ),
    ('AMD', (
            ('RX', 'RX'),
            ('6000Series', '6000Series'),
        )
    ),
    ]
    Product_name = models.CharField(max_length=300, choices = CHOICES, default='Sell')
    Product_Type = models.CharField(max_length=300, choices = CHOICES_CARD, default='Sell')
    author = models.ForeignKey(User,on_delete= models.CASCADE, default='Sell')
    description = models.TextField(max_length=200, default='')
  

    def __str__(self):
        return self.Product_name



