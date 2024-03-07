from django.shortcuts import render
from .models import product
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>App is running</h1>")


def add_product(request):
    records = {
        "url" : "Amazon.com",
        "price" : "10.99"
    }
    product.insert_one(records)
    return HttpResponse("Product has been added")

def get_all_product(request):
    products = product.find()
    return(products)