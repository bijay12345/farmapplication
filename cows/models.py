from django.db import models
from PIL import Image
from datetime import date

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
	image=models.ImageField(upload_to="cowMeicines/",default='cowMedicine.jpg')


	def get_validity(self):
		if self.expiration_date < date.today():
			return True
		else:
			return False

	def get_total_price(self):
		return self.quantity*self.price

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		
		image=Image.open(self.image.path)

		if image.width > 100 or image.height > 100:
			output=(100,100)
			image.thumbnail(output)
			image.save(self.image.path)


class Milk(models.Model):
	price=models.FloatField()
	date=models.DateField()
	quantity=models.FloatField()


	def __str__(self):
		return f"{self.quantity} litres on {self.date}"

	def get_total_milk_sold(self):
		return self.price * self.quantity 

class CowInfo(models.Model):
	cow=models.ForeignKey(Cow,on_delete=models.CASCADE)
	today=models.DateField()
	milking=models.FloatField()


	class Meta:
		ordering=('-today',)

	def __str__(self):
		return f"{self.cow.name} gave {self.milking} litres milk."

