from django.urls import path
from ebooks.urls import ebooks

urlpatterns = [
    path('ebook/<str:category>', ebooks),
]


