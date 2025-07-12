from django.db.models import Count, Q

from .models import Quote


def get_quotes_with_top_n_votes(n=None) -> list[Quote]:
    return Quote.objects.annotate(win_count=Count("winner")).order_by("-win_count")[:n]


def get_quotes_with_top_n_votes_for_user(user_id, n=None) -> list[Quote]:
    return Quote.objects.annotate(
        win_count=Count("winner", filter=Q(winner__user_id=user_id))
    ).order_by("-win_count")[:n]
