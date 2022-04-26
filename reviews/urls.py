from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_details, name='book_details')
    ]
