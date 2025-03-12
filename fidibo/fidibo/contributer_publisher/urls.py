from django.urls import path
from contributer_publisher.views import contributer_page, publisher_page
urlpatterns = [
    path('contributers/<str:author>', contributer_page),
    path('publisher/<str:publisher>', publisher_page)
]
