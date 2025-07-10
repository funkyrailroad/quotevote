from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import VoteOnQuotesVoteForm
from .models import Quote, VoteOnQuotes
from .utils import get_quotes_with_top_n_votes


def home(request):
    return render(request, "app/home.html")


class MostWinsListView(ListView):
    model = Quote
    template_name = "app/mostwins_list.html"
    queryset = get_quotes_with_top_n_votes()


class QuoteListView(ListView):
    model = Quote


class QuoteDetailView(DetailView):
    model = Quote


class QuoteCreateView(CreateView):
    model = Quote
    fields = ["text", "author"]


class QuoteUpdateView(UpdateView):
    model = Quote
    fields = ["text", "author"]


class QuoteDeleteView(DeleteView):
    model = Quote
    success_url = reverse_lazy("quote-list")


class VoteOnQuotesCreateView(CreateView):
    model = VoteOnQuotes
    fields = "__all__"
    success_url = reverse_lazy("vote-on-quotes-list")


class VoteOnQuotesDetailView(DetailView):
    model = VoteOnQuotes


class VoteOnQuotesVoteView(UpdateView):
    model = VoteOnQuotes
    form_class = VoteOnQuotesVoteForm
    template_name_suffix = "_vote"
    success_url = reverse_lazy("vote-on-quotes-create-vote-pair")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vote = self.get_object()
        kwargs["quote_options"] = Quote.objects.filter(
            pk__in=[vote.quote_1.pk, vote.quote_2.pk]
        )
        return kwargs


class VoteOnQuotesListView(ListView):
    model = VoteOnQuotes


def select_two_quotes():
    return Quote.objects.order_by("?")[:2]  # Your logic to select two quotes


@login_required
def create_vote_pair(request):
    quote_1, quote_2 = select_two_quotes()
    vote = VoteOnQuotes.objects.create(
        quote_1=quote_1,
        quote_2=quote_2,
        user=request.user,
    )
    return redirect("vote-on-quotes-vote", pk=vote.pk)
