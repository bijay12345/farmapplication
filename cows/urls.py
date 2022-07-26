from .views import cowadd,medicineadd,cowList,cowDetail
from django.urls import path

urlpatterns=[
	path('cowadd/',cowadd,name="cowAdd"),
	path('cowlist/',cowList,name="cow-list"),
	path('medicineadd/',medicineadd,name="medicineadd"),
	path('cowDetail/<str:pk>',cowDetail,name="cowdetail")
]