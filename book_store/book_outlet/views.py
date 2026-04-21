from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.db.models import Avg

from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all()
    num=books.count()
    avg=round(books.aggregate(Avg('rating'))['rating__avg'] or 0, 1)
    return render(request,'book_outlet/index.html',{
        "books": books,
        'total_number_of_books': num,
        'average_rating':avg
    })

def book_detail(request,slug):
    book=get_object_or_404(Book,slug=slug)
    return render(request,'book_outlet/book_detail.html',{
        'title':book.title,
        'author':book.author,
        'rating':book.rating
    })