#scraper/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('',views.search_form),
    path('login/', views.login, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('add_product/', views.add_product, name='add_product'),

]