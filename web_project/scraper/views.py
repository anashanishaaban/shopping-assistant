from django.shortcuts import render, redirect
from .models import wishlist
from .task import *
from .amazon import *
from .chatbot import *
import os

def index(request):
    return render(request, 'Landing.html')

def login(request):
    return render(request, 'Login.html')

def signup_view(request):
    if request.method == 'POST':
        # Process signup
        return redirect('login')
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'Profile.html')

def wishlist(request):
    return render(request, 'wishlist.html')


def search_results(request):


    search_term = request.GET.get('search_term', '')

    #if search_term:
       #output_csv_path = "C:\\Users\\anoos\\shopping-assistant-2\\web_project\\scraper\\output.csv"


    #if os.path.exists(output_csv_path):
        #os.remove(output_csv_path)


    #api_call(search_term)
    results=get_product_data_csv("output.csv")
    #asins = [product[1] for product in results]
    #fetch_and_save_product_details.delay(asins)
 
    return render(request, 'results.html', {'search_term': search_term, 'products': results})
