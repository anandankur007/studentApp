from django.urls import path
from . import views

urlpatterns = [
    path('order/getOrder/', views.getOrder),
    path('order/placeOrder/', views.createOrder)
]