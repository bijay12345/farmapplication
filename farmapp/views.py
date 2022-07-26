from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Stocks
from .forms import StockForm
from django.contrib import messages


def home(request):
	return render(request,"farmapp/home.html")

def stocks(request):
	stocks=Stocks.objects.all()
	return render(request,"farmapp/stocks.html",{'stocks':stocks})

def stocksDetail(request, pk):
	stock=Stocks.objects.get(id=pk)
	return render(request,'farmapp/stocksdetail.html',{'stock':stock})

def add_stocks(request, id):
	stock=Stocks.objects.get(id=id)
	stock.quantity += 1
	stock.save()
	return redirect('stocks')

def remove_stock(request, id):
	stock=Stocks.objects.get(id=id)
	stock.quantity -= 1
	stock.save()
	return redirect('stocks')

def stockForm(request):
	if request.method == "POST":
		form=StockForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"Stocks added successfully")
			return redirect("stocks")
	else:
		form=StockForm()
	return render(request,'farmapp/stockform.html',{'form':form})