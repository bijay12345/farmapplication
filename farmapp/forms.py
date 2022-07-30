from django import forms
from .models import Stocks,DisplayImage,Schedule
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class DateInput(forms.DateInput):
	input_type= 'date'

class StockForm(forms.ModelForm):
	class Meta:
		model=Stocks
		fields=['name','price','date','quantity','image']
		widgets={
		'date': DateInput()
		}
class DisplayImages(forms.ModelForm):
	class Meta:
		model=DisplayImage  
		fields=['frontdisplayImg','cowDisplay','goatDisplay']

class ScheduleForm(forms.ModelForm):
	class Meta:
		model=Schedule  
		fields=['eventname','category','date']
		widgets={
		'date':DateInput()
		}