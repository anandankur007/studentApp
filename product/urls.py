from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/addItem/', views.additem),
    path('product/deleteItem/', views.deleteitem),
    path('product/getItem', views.getitem),
]