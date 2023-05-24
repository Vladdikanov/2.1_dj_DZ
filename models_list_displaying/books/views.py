from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    print(books)
    context = {"books" : books}
    return render(request, template, context)

def books_date(request,date):
    template = 'books/books_list2.html'
    books = Book.objects.filter(pub_date=date)
    previous_page = Book.objects.filter(pub_date=date).order_by('-pub_date').first()
    next_page = Book.objects.filter(pub_date=date).order_by('pub_date').first()
    print(previous_page.pub_date)
    print(next_page.pub_date)
    context = {"books" : books}
    return render(request, template, context)
