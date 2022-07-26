from django.db import models
from PIL import Image


COW_CHOICES=(
	('SC','SMALL COW'),
	('BC','BIG COW'),
	('NB','NEW BORN'),
	)
GENDER_CHOICES=(
	('M','MALE'),
	('F','FEMALE'),
	('O','OTHERS'),
	)

#Add a daily milk prouction model to keep track of daily productions

class Cow(models.Model):
	name=models.CharField(max_length=100)
	age=models.IntegerField()
	image=models.ImageField(upload_to='cowImages/',default='cowdefault.jpg')
	color=models.CharField(max_length=100)
	breed=models.CharField(max_length=100)
	category=models.CharField(max_length=2,choices=COW_CHOICES)
	gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
	milkAverage=models.FloatField(default=1)

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		
		image=Image.open(self.image.path)

		if image.width > 300 or image.height > 300:
			output=(300,300)
			image.thumbnail(output)
			image.save(self.image.path)


class Medicine(models.Model):
	name=models.CharField(max_length=300)
	price=models.FloatField()
	expiration_date=models.DateField()
	quantity=models.IntegerField(default=1)


	def get_validity(self):
		from django.utils import timezone
		if expiration_date >= timezone.now():
			return f"{self.name} is Applicable"
		else:
			return f"{self.name} is Expired."

	def get_total_price(self):
		return self.quantity*self.price

	def __str__(self):
		return self.name
