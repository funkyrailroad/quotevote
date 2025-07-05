from django.urls import path

from .views import (
    QuoteCreateView,
    QuoteDeleteView,
    QuoteDetailView,
    QuoteListView,
    QuoteUpdateView,
    VoteOnQuotesCreateView,
    VoteOnQuotesDetailView,
    VoteOnQuotesListView,
    VoteOnQuotesVoteView,
    create_vote_pair,
    home,
)

# app_name = "app"
urlpatterns = [
    path("", home, name="home"),
    path("quotes", QuoteListView.as_view(), name="quote-list"),
    path("quotes/<int:pk>", QuoteDetailView.as_view(), name="quote-detail"),
    path("quotes/create", QuoteCreateView.as_view(), name="quote-create"),
    path("quotes/<int:pk>/update", QuoteUpdateView.as_view(), name="quote-update"),
    path("quotes/<int:pk>/delete", QuoteDeleteView.as_view(), name="quote-delete"),
    path(
        "vote-on-quotes",
        VoteOnQuotesListView.as_view(),
        name="vote-on-quotes-list",
    ),
    path(
        "vote-on-quotes/create-vote-pair",
        create_vote_pair,
        name="vote-on-quotes-create-vote-pair",
    ),
    path(
        "vote-on-quotes/create",
        VoteOnQuotesCreateView.as_view(),
        name="vote-on-quotes-create",
    ),
    path(
        "vote-on-quotes/<int:pk>",
        VoteOnQuotesDetailView.as_view(),
        name="vote-on-quotes-detail",
    ),
    path(
        "vote-on-quotes/<int:pk>/vote",
        VoteOnQuotesVoteView.as_view(),
        name="vote-on-quotes-vote",
    ),
]
