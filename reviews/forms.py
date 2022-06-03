from django import forms
from .models import Publisher, Review, Book

SEARCH_CHOICES = (
    ("title", "Title"),
    ("contributor", "Contributor")
    )


class SearchForm(forms.Form):
    """Basic Search Form, it will work with a minimum of 3 characters, selecting if you want to search
    by Title or Contributor, and neither of them is required for the form to work. By default, search is set
    to search_in by Title."""
    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Review
        exclude = ("date_edited", "book")


class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("cover", "sample")
