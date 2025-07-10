from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Quote, VoteOnQuotes
from .utils import get_quotes_with_top_n_votes


class Tests(TestCase):
    fixtures = ["quotes.json"]

    def test_1(self):
        objs = Quote.objects.all()


class QuoteVoteWinsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser")

        self.quote_1 = Quote.objects.create(text="Quote 1", author="Author 1")
        self.quote_2 = Quote.objects.create(text="Quote 2", author="Author 2")
        self.quote_3 = Quote.objects.create(text="Quote 3", author="Author 3")

        self.vote_1 = VoteOnQuotes.objects.create(
            quote_1=self.quote_1,
            quote_2=self.quote_2,
            winner=self.quote_1,
            user=self.user,
        )
        self.vote_2 = VoteOnQuotes.objects.create(
            quote_1=self.quote_1,
            quote_2=self.quote_3,
            winner=self.quote_1,
            user=self.user,
        )
        self.vote_3 = VoteOnQuotes.objects.create(
            quote_1=self.quote_2,
            quote_2=self.quote_3,
            winner=self.quote_2,
            user=self.user,
        )

    def test_counts_and_ordering(self):
        quotes = get_quotes_with_top_n_votes()

        quote_1 = quotes[0]
        self.assertEqual(quote_1.win_count, 2)

        quote_2 = quotes[1]
        self.assertEqual(quote_2.win_count, 1)

        quote_3 = quotes[2]
        self.assertEqual(quote_3.win_count, 0)
