from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from .models import Books


# Create your views here.
def get_books(request):
    info = list(Books.objects.values_list('name', 'author', 'category', 'page_count', 'price', 'cover'))
    return JsonResponse(info, safe=False)


def get_book(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        return render(request, 'info.html', context={'book': book})

    except Books.DoesNotExist:
        return JsonResponse({'ERROR': 'THE BOOK WITH THIS ID IS NOT AVAILABLE'}, status=404)


def home(request):
    return render(request, 'home.html')


def book_list(request):
    books = Books.objects.all().order_by('price')
    paginator = Paginator(books, 3)
    page = int(request.GET.get('page', 1))
    try:
        page = int(page)
    except ValueError:
        page = 1
    books = paginator.get_page(page)
    return render(request, 'shop.html', {'books': books})
