from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-rating')
    number_of_books = books.count()
    average_rating = books.aggregate(Avg('rating')).get('rating__avg')
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_books': number_of_books,
        'average_rating': average_rating
    })
    
def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404
    return render(request, 'book_outlet/book_detail.html', {
        'book': book
    })