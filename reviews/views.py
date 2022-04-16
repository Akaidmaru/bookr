from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    book_name = request.GET.get("book_name") or "None"
    return render(request, "search_result.html", {"book_name": book_name})
