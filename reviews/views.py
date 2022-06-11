from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.core.files.images import ImageFile
from io import BytesIO
from PIL import Image


from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from .forms import PublisherForm, SearchForm, ReviewForm, BookMediaForm


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(first_names__icontains=search)

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(last_names__icontains=search)

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(request, "search_result.html", {"form": form, "search_text": search_text, "books": books})


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)

        else:
            book_rating = None
            number_of_reviews = 0

        book_list.append({
            'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews
        })
    context = {'book_list': book_list}
    return render(request, 'reviews/books_list.html', context)


def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.review_set.all()

    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {"book": book, "book_rating": book_rating, "reviews": reviews}
    else:
        context = {"book": book, "book_rating": None, "reviews": reviews}

    return render(request, 'reviews/book_details.html', context)

# @permission_required('edit_publisher')


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
        if publisher is None:
            messages.success(request, f"Publisher '{updated_publisher}' was created.")
        else:
            messages.success(request, f"Publisher '{updated_publisher}' was updated.")
        return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "reviews/instance-form.html", {
        "form": form, "instance": publisher, "model_type": "Publisher"})


@login_required
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, id=book_pk)
    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, id=review_pk)
        user = request.user
        if not user.is_staff and review.creator.id != user.id:
            raise PermissionDenied
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.book = book
        if review_pk is None:
            messages.success(request, f"Review for '{book}' was created.")

        else:
            messages.success(request, f"Review for '{book}' updated.")
            updated_review.date_edited = timezone.now()
            updated_review.save()

        return redirect('book_details', book.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/instance-form.html", {
        "form": form,
        "instance": review,
        "model_type": "Review",
        "related_model_type": "Book",
        "related_instance": book})


@login_required
def book_media(request, book_pk):
    book = get_object_or_404(Book, id=book_pk)

    if request.method == 'POST':
        form = BookMediaForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(False)
            cover = form.cleaned_data.get("cover")
            if cover:
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)

            book.save()
            messages.success(request, f"Book {book}' was successfully updated.")
            return redirect('book_details', book.id)
    else:
        form = BookMediaForm(instance=book)

    return render(request, "reviews/instance-form.html", {
        "form": form,
        "instance": book,
        "model_type": "Book",
        "is_file_upload": True,
        })
