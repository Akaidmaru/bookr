from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    book_name = request.GET.get("book_name") or "None"
    return render(request, "search_result.html", {"book_name": book_name})


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
