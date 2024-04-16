#scraper/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('',views.search_form, name='landing'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('add_product/', views.add_product, name='add_product'),
    path('landing/', views.search_results, name='search_results'),
    path('profile/', views.profile, name='profile'),
]