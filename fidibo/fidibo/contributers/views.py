from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def contributer_page(request):
    return HttpResponse(f"this page is dedicated to contributers")