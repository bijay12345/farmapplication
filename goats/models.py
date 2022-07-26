from django.db import models
from PIL import Image


GOAT_CHOICES=(
	('SG',"SMALL GOAT"),
	('BG',"BIG GOAT"),
	('NB',"NEW BORN"),
	)

class Goat(models.Model):
	name=models.CharField(max_length=100)
	age=models.IntegerField()
	image=models.ImageField(upload_to='GoatImages/',default='goatdefault.jpg')
	breed=models.CharField(max_length=100)
	color=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	category=models.CharField(max_length=2,choices=GOAT_CHOICES)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super().save(*args,**kwargs)

		image=Image.open(self.image.path)

		if image.width > 200 or image.height > 200:
			output=(200,200)
			image.thumbnail(output)
			image.save(self.image.path)


class Medicines(models.Model):
	name=models.CharField(max_length=300)
	expiration_date=models.DateField()
	price=models.FloatField()
	quantity=models.IntegerField(default=1)

	def __str__(self):
		return self.name