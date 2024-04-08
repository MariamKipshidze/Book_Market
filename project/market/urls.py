from django.urls import path
from .views import get_book, get_books

urlpatterns = [
    path('books/<int:book_id>', get_book, name='get_book'),
    path('books/', get_books, name='get_books')
]
