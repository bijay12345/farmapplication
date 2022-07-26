from django.db import models
from django.shortcuts import reverse

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


