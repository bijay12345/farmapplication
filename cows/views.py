from django.shortcuts import render,redirect
from .forms import CowForm,MedicineForm
from .models import Cow


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
	cows=Cow.objects.all()
	return render(request,'cows/cows.html',{'cows':cows})

def cowDetail(request,pk):
	cow=Cow.objects.get(id=pk)
	return render(request,"cows/cowDetail.html",{'cow':cow})