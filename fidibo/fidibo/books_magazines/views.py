from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def ebooks(request, category: str):
    return HttpResponse(f"this page shows the books of ebook {category}")

def audiobooks(request, category: str):
    return HttpResponse(f"this page shows the books of audiobook {category}")

def magazines(request, category: str):
    return HttpResponse(f"this page shows the magazines of {category}")

def education(request, category: str):
    return HttpResponse(f"this page shows the educational books of {category}")

def education(request, name: str):
    return HttpResponse(f"this page shows the details of {name}")
