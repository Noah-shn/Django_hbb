from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class produit(models.Model):
	CARD_CHOISES=[(None,'Nvidia'),('AMD','AMD'),
				('intel','intel')]
	#CSC=card series choice
	CSC_CHOISES=(('Rtx 3060ti','Rtx 3060ti'),('5700xt','5700xt'),
				('A380','A380'))
	

	choix = models.ForeignKey(User,on_delete=models.CASCADE, choices = CARD_CHOISES)
	serie= models.CharField(max_length=12, choices=CSC_CHOISES)