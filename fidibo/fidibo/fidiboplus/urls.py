from django.urls import path
from fidiboplus.views import features, main


urlpatterns = [
    path('', main),
    path('<str:features>', features)
]
