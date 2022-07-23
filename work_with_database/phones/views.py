from django.shortcuts import render, redirect
from phones.models import Phone
def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    if sort_by == 'min_price':
        sort_by = 'price'
    if sort_by == 'max_price':
        sort_by = '-price'
    if sort_by == None:
        sort_by = 'name'
    context = {
        'phones' : Phone.objects.all().order_by(sort_by)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone':  Phone.objects.get(slug=slug)}
    return render(request, template, context)
