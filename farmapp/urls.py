from django.urls import path
from .views import home,add_stocks,stocksDetail,remove_stock,stockForm,displayImages,eventForm


urlpatterns=[
	path('',home,name="home"),
	path('add_stocks/<str:id>',add_stocks,name="add_stocks"),
	path('remove_stock/<str:id>',remove_stock,name="remove_stock"),
	path('stocksDetail/<str:pk>',stocksDetail,name="stocksDetail"),
	path('stockform/',stockForm,name="stockform"),
	path('display/',displayImages,name="displays"),
	path('eventForm/',eventForm,name="eventform")
]