from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def contributer_page(request, author: str):
    return HttpResponse(f"this page is dedicated to {author}")

def publisher_page(request, publisher):
    return HttpResponse(f"this page is dedicated to {publisher}")