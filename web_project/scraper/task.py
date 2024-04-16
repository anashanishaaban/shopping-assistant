from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import *
import requests
import json


from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json


@shared_task
def asin_api_call(asin):
    api_key = '7E9E4E160584452791B7CB9E8829AACD'
    base_url = 'https://api.rainforestapi.com/request'
    amazon_domain = 'amazon.com'
    all_product_details = []
    params = {
        'api_key': api_key,
        'type': 'product',
        'asin': asin,
        'amazon_domain': amazon_domain
    }

    response = requests.get(base_url, params=params)
    product_data = response.json()

    # Process and concatenate product details into a single string (or a structured format as needed)
    product_details = json.dumps(product_data)
    all_product_details.append(product_details)
    with open('product_details.txt', 'w') as file:
        for detail in all_product_details:
            file.write(detail + "\n")

@shared_task
def fetch_and_save_product_details(asin_list):
    for asin in asin_list:
        asin_api_call.delay(asin)