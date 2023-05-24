from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    print(request.GET)
    try:
        if request.GET["sort"] == "name":
            phones = Phone.objects.order_by("name")
        elif request.GET["sort"] == 'min_price':
            phones = Phone.objects.order_by("price")
        elif request.GET["sort"] == 'max_price':
            phones = Phone.objects.order_by("-price")
    except:
        phones = Phone.objects.all()
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_obj = Phone.objects.filter(slug=slug)
    context = {"phone" : phone_obj[0]}
    return render(request, template, context)
