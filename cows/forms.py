from django import forms
from .models import Medicine, Cow


class CowForm(forms.ModelForm):
	class Meta:
		model=Cow  
		fields=['name','age','color','breed','category','gender','milkAverage','image']

class MedicineForm(forms.ModelForm):
	class Meta:
		model=Medicine
		fields=['name','price','expiration_date','quantity']