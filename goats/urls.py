from django.urls import path
from .views import goatadd,medicineadd,gaotList,goatDetail


urlpatterns=[
	path('goatform/',goatadd,name='goatadd'),
	path("gaotList/",gaotList,name="goat-list"),
	path('medicineadd/',medicineadd,name="goatMedicine"),
	path('goatdetails/<str:pk>',goatDetail,name="goat-detail")
]