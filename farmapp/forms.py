from django import forms
from .models import Stocks
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class StockForm(forms.ModelForm):
	class Meta:
		model=Stocks
		fields=['name','price','date','quantity','image']