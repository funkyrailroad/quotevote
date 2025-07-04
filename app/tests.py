from django.test import TestCase

from .models import Quote


class Tests(TestCase):
    fixtures = ["quotes.json"]

    def test_1(self):
        objs = Quote.objects.all()
