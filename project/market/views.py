from django.http import JsonResponse
from .models import Books


# Create your views here.
def get_books(request):
    books = Books.objects.all()
    book_list = []
    for book in books:
        book_list.append({
            'Name': book.name,
            'Author': book.author,
            'Category': book.category,
            'Page_count': book.page_count,
            'Price': book.price,
            'id': book.id
        })
    return JsonResponse(book_list, safe=False)


def get_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    book_info = {
        'Name': book.name,
        'Author': book.author,
        'Category': book.category,
        'Page_count': book.page_count,
        'Price': book.price,
        'id': book.id
    }
    return JsonResponse(book_info)
