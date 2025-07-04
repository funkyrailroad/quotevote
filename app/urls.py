# include urls
from django.urls import path

from .views import quotes_list

urlpatterns = [
    path("quotes", quotes_list, name="quotes_list"),
]
