from django.shortcuts import render, redirect
from .models import product
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

def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        response = openai_call(prompt)
        return render(request, 'chatbot.html', {'response': response})
    return render(request, 'chatbot.html')

def add_product(request):


    search_term = request.GET.get('search_term', '')

    #if search_term:
       #output_csv_path = "C:\\Users\\anoos\\shopping-assistant-2\\web_project\\scraper\\output.csv"


    #if os.path.exists(output_csv_path):
        #os.remove(output_csv_path)


    #api_call(search_term)
    results=get_product_data_csv("output.csv")
    #asins = [product[1] for product in results]
    #fetch_and_save_product_details.delay(asins)
    # Now, iterate through the results and add them to the database
    #for data in results:
        #add_product_data_to_db(data)

    return render(request, 'Results.html', {'products': results})

def search_results(request):
    search_term = request.GET.get('search_term')
    # Retrieve the products based on the search_term
    products = get_product_data_csv("output.csv")  # Your logic to fetch the products based on the search term
    return render(request, 'results.html', {'search_term': search_term, 'products': products})