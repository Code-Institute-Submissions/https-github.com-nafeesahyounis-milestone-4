from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('cart/add_to_cart/<product_id>', views.add_to_cart, name='add_to_cart')
]
