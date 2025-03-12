from django.urls import path
from search.views import show_product

urlpatterns = [
    path('<str:city>/<str:product>', show_product)
]
