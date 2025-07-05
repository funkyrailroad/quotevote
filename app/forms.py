from django import forms

from .models import VoteOnQuotes


class VoteOnQuotesVoteForm(forms.ModelForm):
    class Meta:
        model = VoteOnQuotes
        fields = ["winner"]

    def __init__(self, *args, **kwargs):
        quote_options = kwargs.pop("quote_options", None)
        super().__init__(*args, **kwargs)

        if quote_options is not None:
            self.fields["winner"].queryset = quote_options
