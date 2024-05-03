from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')
        print(f'{name} / {phone} / {message}')
        data = f'Name: {name}. Phone: {phone}. Message: {message}\n'
        with open('user_data.txt', 'a', encoding='UTF-8') as f:
            f.write(data)
    return render(requests, 'catalog/contacts.html')


def products_list(requests):
    products = Product.objects.all()
    context = {'products': products}
    return render(requests, 'catalog/products_list.html', context)


def product_info(requests, pk):
    product = get_object_or_404(Product, pk=pk)
    # product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(requests, 'catalog/product_info.html', context)
