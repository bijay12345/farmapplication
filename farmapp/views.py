from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Stocks, DisplayImage,Schedule
from .forms import StockForm,DisplayImages,ScheduleForm
from django.contrib import messages
from cows.models import CowInfo
from datetime import date
	

def home(request):
	today=date.today()
	stocks=Stocks.objects.all()
	infos=CowInfo.objects.filter(today=today)
	displays=DisplayImage.objects.all()
	futureschedules=Schedule.objects.all().filter(date__gt=today)
	pastSchedules=Schedule.objects.all().filter(date__lt=today)
	return render(request,"farmapp/home.html",{"infos":infos,"displays":displays,\
		"stocks":stocks,"futureschedules":futureschedules,'pastSchedules':pastSchedules})	

def stocksDetail(request, pk):
	stock=Stocks.objects.get(id=pk)
	return render(request,'farmapp/stocksdetail.html',{'stock':stock})

def add_stocks(request, id):
	stock=Stocks.objects.get(id=id)
	stock.quantity += 1
	stock.save()
	return redirect('/')

def remove_stock(request, id):
	stock=Stocks.objects.get(id=id)
	stock.quantity -= 1
	stock.save()
	return redirect('/')

def stockForm(request):
	if request.method == "POST":
		form=StockForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"Stocks added successfully")
			return redirect("add_stocks")
	else:
		form=StockForm()
	return render(request,'farmapp/stockform.html',{'form':form})

def displayImages(request):
	if request.method == "POST":
		form=DisplayImages(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"image added successfully")
			return redirect("displays")
	else:
		form=DisplayImages()
	return render(request,'farmapp/stockform.html',{'form':form})

def eventForm(request):
	if request.method == "POST":
		form=ScheduleForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"event added successfully")
			return redirect('/')
	else:
		form=ScheduleForm()
	return render(request,'farmapp/eventform.html',{'form':form})
