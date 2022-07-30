from django import forms
from .models import Medicine, Cow, CowInfo


class DateInput(forms.DateInput):
	input_type= 'date'

class CowForm(forms.ModelForm):
	class Meta:
		model=Cow  
		fields=['name','age','color','breed','category','gender','milkAverage','image']

class MedicineForm(forms.ModelForm):
	class Meta:
		model=Medicine
		fields=['name','price','image','expiration_date','quantity']
		widgets={'expiration_date': DateInput()}

class CowInfoForm(forms.ModelForm):
	class Meta:
		model=CowInfo 
		fields=['cow','milking','today']
		widgets={
		'today': DateInput()
		}