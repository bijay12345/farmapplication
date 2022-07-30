from django.shortcuts import render,redirect
from .models import Goat
from .forms import GoatForm,MedicineForm
from farmapp.models import DisplayImage


def goatadd(request):
	if request.method=="POST":
		form=GoatForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("goat-list")
	else:
		form=GoatForm()
	return render(request,"goats/goatform.html",{"form":form})


def medicineadd(request):
	if request.method=="POST":
		form=MedicineForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		form=MedicineForm()
	return render(request,"goats/medicineForm.html",{"form":form})


def gaotList(request):
	displays=DisplayImage.objects.all()
	goats=Goat.objects.all()
	return render(request,'goats/goatlist.html',{'goats':goats,'displays':displays})


def goatDetail(request,pk):
	goat=Goat.objects.get(id=pk)
	return render(request,"goats/goatDetail.html",{'goat':goat})

