#scraper/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='landing'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('landing/', views.search_results, name='search_results'),
    path('profile/', views.profile, name='profile'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('analyze-image/', views.analyze_image, name='analyze_image'),
]