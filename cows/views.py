from django.shortcuts import render,redirect
from .forms import CowForm,MedicineForm,CowInfoForm
from .models import Cow, Medicine,CowInfo
from farmapp.models import DisplayImage, Medical
from datetime import date



def cowadd(request):
	if request.method=="POST":
		form=CowForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("cowAdd")
	else:
		form=CowForm()
	return render(request,"cows/cowForm.html",{"form":form})


def medicineadd(request):
	if request.method=="POST":
		form=MedicineForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		form=MedicineForm()
	return render(request,"cows/medicineForm.html",{"form":form})

def cowList(request):
	today=date.today()
	displays=DisplayImage.objects.all()
	infos=CowInfo.objects.filter(today=today)
	cows=Cow.objects.all()
	return render(request,'cows/cows.html',{'cows':cows,'displays':displays,'infos':infos})

def cowDetail(request,pk):
	cow=Cow.objects.get(id=pk)
	return render(request,"cows/cowDetail.html",{'cow':cow})


def medicineList(request):
	medicines=Medicine.objects.all()
	return render(request,"cows/medicineList.html",{"medicines":medicines})

def milkInfo(request):
	if request.method=="POST":
		form=CowInfoForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("milkInfo")
	else:
		form=CowInfoForm()
	return render(request,"cows/cowinfoform.html",{"form":form})


