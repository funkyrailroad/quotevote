from django.db.models import Count

from .models import Quote


def get_quotes_with_top_n_votes(n=None) -> list[Quote]:
    return Quote.objects.annotate(win_count=Count("winner")).order_by("-win_count")[:n]
