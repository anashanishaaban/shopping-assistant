from django.shortcuts import render, redirect
from .models import wishlist
from .task import *
from .amazon import *
from .chatbot import *
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai

@csrf_exempt
def analyze_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        OPEN_AI_KEY = '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'
        client = OpenAI(api_key=OPEN_AI_KEY)

        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What’s in this image?"},
                        {
                            "type": "image_url",
                            "image_url": image_url,
                        },
                    ],
                }
            ],
            max_tokens=300,
        )

        description = response.choices[0].message['content'] if response.choices else 'No description found.'
        return JsonResponse({'description': description})

    return JsonResponse({'error': 'This endpoint supports only POST method.'}, status=405)

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
