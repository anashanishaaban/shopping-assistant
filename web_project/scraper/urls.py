#scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.search_form),
    path('add/', views.add_product, name='add_product'),    
]