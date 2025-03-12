from django.urls import path
from fidiboplus.views import features


urlpatterns = [
    path('<str:features>', features)
]
