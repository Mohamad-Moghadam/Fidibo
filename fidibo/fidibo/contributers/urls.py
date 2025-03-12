from django.urls import path
from contributers.views import contributer_page

urlpatterns = [
    path('contributers/<str:author>')
]
