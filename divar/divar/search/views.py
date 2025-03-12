from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

products = {
    'name' : 'name',
    'price' : 'price',
    'sellers number' : 'number',
    'product photo' : 'the photo',
    'description' : 'description',
    'category' : 'category'
}

def show_product(request, product):
    products['category'] = product
    return JsonResponse(products)
