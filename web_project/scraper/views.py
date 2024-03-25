from django.shortcuts import render
from .models import product
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import csv
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import datetime
import smtplib
import pandas as pd
import os
import openai
from openai import OpenAI
from .task import *
from .amazon import *
from .chatbot import *

def add_product_data_to_db(data):
    # Assuming your Product model has fields corresponding to the data list items
    # e.g., URL, Title, Price, Ratings, Score, Review Summary
    # Adapt field names based on your actual model definition
    records = {
        "url": str(data[0]),
        "title" : str(data[1]),
        "price " : str(data[2]),
        "ratings": str(data[3]),
        "score" : str(data[4]),
        "review_summary" : str(data[5])
    }
    product.insert_one(records)

def search_form(request):
    return render(request, 'search_bar.html')

def add_product(request):


    search_term = request.GET.get('search_term', '')

    if search_term:
        output_csv_path = "C:\\Users\\anoos\\shopping-assistant-2\\web_project\\scraper\\output.csv"

    if os.path.exists(output_csv_path):
        os.remove(output_csv_path)
    

    api_call(search_term)
    results=get_product_data_csv("output.csv")
    #print(results)
    #asins = [product[1] for product in results]
    #fetch_and_save_product_details.delay(asins)
    # Now, iterate through the results and add them to the database
    #for data in results:
        #add_product_data_to_db(data)
    
    # Instead of returning an HttpResponse, render the template with the results
    return render(request, 'add_products.html', {'products': results})


