#scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add/', views.add_product),
    path('show/', views.get_all_product),
]