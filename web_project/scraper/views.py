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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-65c58daf-3a2c6c3a7adb35726b652acb"
}

'''
AMAZON
'''

'''
def get_product_links_amazon(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    a_tag = soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    product_link_list = []
    for tag in a_tag:
        href = tag.get('href', '')
        # Check if href is a complete URL or a relative path
        if href.startswith('http'):
            product_link_list.append(href)
        else:
            # Ensure it's a relative path and prepend the base URL
            product_link_list.append('https://www.amazon.com' + href)
            
    return product_link_list


def get_product_data_amazon(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id='productTitle').get_text().strip() if soup.find(id='productTitle') else 'N/A'
    price = soup.find('span', class_='a-offscreen').get_text().strip() if soup.find('span', class_='a-offscreen') else 'N/A'
    rating = soup.find('span', id='acrCustomerReviewText').get_text().strip() if soup.find('span', id='acrCustomerReviewText') else 'N/A'
    score = soup.find('span', class_='a-icon-alt').get_text().strip() if soup.find('span', class_='a-icon-alt') else 'N/A'
    review_summary = soup.find(id='product-summary').get_text().strip() if soup.find(id='product-summary') else 'N/A'

    return [url, title, price, rating, score, review_summary]
'''

def api_call(search_term):

    # Set up the request parameters
    params = {
        'api_key': '7E9E4E160584452791B7CB9E8829AACD',
        'type': 'search',
        'amazon_domain': 'amazon.com',
        'search_term': search_term,
        'output': 'csv'
    }

    # Make the HTTP GET request to Rainforest API
    api_result = requests.get('https://api.rainforestapi.com/request', params)

    # Save the CSV response to a file
    with open('output.csv', 'wb') as file:
        file.write(api_result.content)
        

def get_product_data_csv(file_path):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Selecting the required columns
    selected_columns = [
        'search_results.title', 
        'search_results.asin', 
        'search_results.link', 
        'search_results.image', 
        'search_results.rating', 
        'search_results.ratings_total', 
        'search_results.is_prime', 
        'search_results.sponsored', 
        'search_results.price.currency', 
        'search_results.price.value'
    ]
    
    # Ensure all columns exist, fill missing with 'N/A'
    for col in selected_columns:
        if col not in data.columns:
            data[col] = 'N/A'
    
    # Select the required columns
    selected_data = data[selected_columns]
    
    # Convert boolean to string for consistency with the original function
    selected_data['search_results.is_prime'] = selected_data['search_results.is_prime'].map({True: 'Prime', False: 'Non-Prime', pd.NA: 'N/A'})
    selected_data['search_results.sponsored'] = selected_data['search_results.sponsored'].map({True: 'Sponsored', False: 'Not Sponsored', pd.NA: 'N/A'})
    
    # Convert the DataFrame to a list of dictionaries for easier processing
    products_list = selected_data.to_dict(orient='records')
    
    # Convert each product into a list format
    products_data = []
    for product in products_list:
        product_data = [
            product['search_results.title'],
            product['search_results.asin'],
            product['search_results.link'],
            product['search_results.image'],
            str(product['search_results.rating']) if product['search_results.rating'] != 'N/A' else product['search_results.rating'],
            str(product['search_results.ratings_total']),
            product['search_results.is_prime'],
            product['search_results.sponsored'],
            product['search_results.price.currency'],
            str(product['search_results.price.value']) if product['search_results.price.value'] != 'N/A' else product['search_results.price.value']
        ]
        products_data.append(product_data)
    
    return products_data

def index(request):
    return HttpResponse("<h1>App is running</h1>")


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
    '''
    # Using ThreadPoolExecutor to concurrently fetch product data
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_product_data_csv))
        print(results)
    '''
    search_term = request.GET.get('search_term', '')
    if search_term:
    # Define the path to the output.csv file
        output_csv_path = "C:\\Users\\anoos\\shopping-assistant-2\\web_project\\scraper\\output.csv"

    # Check if the output.csv file exists
    if os.path.exists(output_csv_path):
        # If it exists, delete the file
        os.remove(output_csv_path)

    api_call(search_term)
    results=get_product_data_csv("output.csv")
    print(results[:5])

    # Now, iterate through the results and add them to the database
    #for data in results:
        #add_product_data_to_db(data)
    
    # Instead of returning an HttpResponse, render the template with the results
    return render(request, 'add_products.html', {'products': results})
