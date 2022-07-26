from django import forms
from .models import Medicines, Goat


class GoatForm(forms.ModelForm):
	class Meta:
		model=Goat  
		fields=['name','age','color','breed','category','gender','image']

class MedicineForm(forms.ModelForm):
	class Meta:
		model=Medicines
		fields=['name','price','expiration_date','quantity']