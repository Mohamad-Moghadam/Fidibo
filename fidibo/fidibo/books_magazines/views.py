from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from books_magazines.models import Ebooks, Audiobook, Magazines


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

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body())

        if data.get("type") == "ebook":
            Ebooks.objects.create(
                name = data.get("name"),
                author = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher = data.get("publisher"),
                time_to_read = data.get("time_to_read"),
                date_of_publish = data.get("date_of_publish"),
                describtion = data.get("describtion"),
                language = data.get("language"),
                volume = data.get("volume"),
            )

        elif data.get("type") == "audiobook":
            Audiobook.objects.create(
                name = data.get("name"),
                author = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher = data.get("publisher"),
                date_of_publish = data.get("date_of_publish"),
                narrator = data.get("narrator"),
                describtion = data.get("describtion"),
                language = data.get("language"),
                volume = data.get("volume"),
            )

        elif data.get("type") == "magazine":
            Magazines.objects.create(
                name = data.get("name"),
                author = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher = data.get("publisher"),
                time_to_read = data.get("time_to_read"),
                date_of_publish = data.get("date_of_publish"),
                describtion = data.get("describtion"),
                language = data.get("language"),
                volume = data.get("volume"),
            )
