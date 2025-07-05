from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author}'

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def get_absolute_url(self):
        return reverse("quote-detail", kwargs={"pk": self.pk})


class VoteOnQuotes(models.Model):
    quote_1 = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="quote_1")
    quote_2 = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="quote_2")
    winner = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        related_name="winner",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="votes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote by {self.user} for {self.winner}"

    def get_absolute_url(self):
        return reverse("vote-on-quotes-detail", kwargs={"pk": self.pk})
