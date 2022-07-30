from django.db import models
from django.shortcuts import reverse
from PIL import Image
from cows.models import Cow  
from goats.models import Goat

class Stocks(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(upload_to='stockImages/',default="Stockdefault.jpg")
	price=models.FloatField()
	date=models.DateField()
	quantity=models.IntegerField(default=1)

	def get_total_price(self):
		return self.quantity*self.price

	def add_stocks_url(self):
		return reverse('add_stocks',kwargs={'id':self.id})

	def remove_stocks_url(self):
		return reverse('remove_stock',kwargs={'id':self.id})

	def __str__(self):
		return f"{self.quantity} {self.name} is in stock."


class DisplayImage(models.Model):
	frontdisplayImg=models.ImageField(upload_to="display_img/",default="defaultDisplay.jpg", null=True,blank=True)
	cowDisplay=models.ImageField(upload_to="cowImage/",default="cowDisplay.jpg", null=True,blank=True)
	goatDisplay=models.ImageField(upload_to="goatImage/",default="goatDefault.jpg", null=True,blank=True)

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		frontimage=Image.open(self.frontdisplayImg.path)
		cowimg=Image.open(self.cowDisplay.path)
		goatimg=Image.open(self.goatDisplay.path)

		if frontimage.width > 600 or frontimage.height > 600:
			output=(600,600)
			frontimage.thumbnail(output)
			frontimage.save(self.frontdisplayImg.path)

		if cowimg.width > 600 or cowimg.height > 600:
			output=(600,600)
			cowimg.thumbnail(output)
			cowimg.save(self.cowDisplay.path)

		if goatimg.width > 600 or goatimg.height > 600:
			output=(600,600)
			goatimg.thumbnail(output)
			goatimg.save(self.goatDisplay.path)

	def get_front_display(self):
		return self.frontdisplayImg.url

	def get_cow_display(self):
		return self.cowDisplay.url

	def get_goat_display(self):
		return self.goatDisplay.url


eventCategory=(
	('C','COW'),
	('G','GOAT'),
	('O','OTHERS')
	)

class Schedule(models.Model):
	eventname=models.CharField(max_length=300)
	category=models.CharField(max_length=1,choices=eventCategory)
	date=models.DateField()

	def __str__(self):
		return f'{self.eventname} on {self.date}'

	class Meta:
		ordering=['date']


class Medical(models.Model):
	name=models.CharField(max_length=300)
	reason=models.CharField(max_length=300)
	cow=models.ForeignKey(Cow,on_delete=models.CASCADE,null=True,blank=True)
	goat=models.ForeignKey(Goat,on_delete=models.CASCADE,null=True,blank=True)
	date=models.DateField()


	def __str__(self):
		return f"{self.name} on {self.date}"

