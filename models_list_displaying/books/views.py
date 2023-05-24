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
    context = {"books": books}
    try:
        previous_page = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
        context["previous_page"] = str(previous_page.pub_date)
    except:
        context["previous_page"] = None
    try:
        next_page = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()
        context["next_page"] = str(next_page.pub_date)
    except:
        context["next_page"] = None
    print(context)
    # print(previous_page.pub_date)
    # print(next_page.pub_date)
    return render(request, template, context)
