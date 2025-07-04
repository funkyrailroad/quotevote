from django.shortcuts import render

from .models import Quote


# list quotes
def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, "quotes/quotes_list.html", {"quotes": quotes})
