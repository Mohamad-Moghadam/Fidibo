from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def ebooks(request, category: str):
    return HttpResponse(f"this page shows the books of ebook category")