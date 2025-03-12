from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def features(request, features: str):
    return HttpResponse(f'this is the {features} page!')

def main(request):
    return HttpResponse(f'this is the main page')
