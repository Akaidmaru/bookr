from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_details, name='book_details'),
    path('book_search/', views.book_search, name='book_search'),
    path('books/<int:book_pk>/reviews/new', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>', views.review_edit, name='review_edit'),
    path('books/<int:book_pk>/media', views.book_media, name='book_media'),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(), name='login')
    ]
