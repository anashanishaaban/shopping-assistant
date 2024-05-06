from django.shortcuts import render, redirect
from .models import wishlist
from .task import *
from .amazon import *
from .chatbot import *
import os
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai

client = openai.OpenAI(api_key="sk-proj-velign6aK9GNDezmvZZAT3BlbkFJiqUX5lJuZvq3eAK2spD4")

@csrf_exempt
def api_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON data from the request body
            message = data.get("message", "")  # Get the 'message' field from JSON
            file_path = data.get("file_path", "output.csv")  # Path to the CSV file containing product data

            # Get product data as a formatted text string
            product_data_text = get_product_data_as_text(file_path)

            # Assume 'client' is already initialized with your OpenAI API key
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI shopping assistant. Use the following product data to answer questions and provide recommendations: " + product_data_text
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            # Check if the response contains a message and return it
            response_text = chat_completion.choices[0].message.content.strip()
            if response_text:
                return HttpResponse(response_text, content_type='text/plain', status=200)
            else:
                return JsonResponse({"error": "Failed to generate response"}, status=500)

        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON format", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred processing your request", "details": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def index(request):
    return render(request, 'Landing.html')

def login(request):
    return render(request, 'Login.html')

def signup_view(request):
    if request.method == 'POST':
        # Process signup
        return redirect('login')
    return render(request, 'signup.html')

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
