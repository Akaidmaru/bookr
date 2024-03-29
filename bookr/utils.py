import datetime

from django.db.models import Count
from reviews.models import Review


def get_books_read_by_month(username):
    """Get the books read by the user on per month basis.
    :param username: str, The username for which the books need to be returned.
    :return: dict of month wise books read.
    """
    current_year = datetime.datetime.now().year
    books = Review.objects.filter(creator__username__contains=username, date_created__year=current_year).values(
        'date_created__month').annotate(book_count=Count('book__title'))
    return books


def get_books_read(username):
    """
    :param username: str, The username for which the books needs to be returned.
    :return: dict of all books read by user.
    """
    books = Review.objects.filter(creator__username__contains=username).all()
    return [{'title': book_read.book.title, 'completed_on': book_read.date_created} for book_read in books]
