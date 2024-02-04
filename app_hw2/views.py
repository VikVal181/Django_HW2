from django.shortcuts import render
from datetime import datetime, timedelta
from app_hw2.models import Client, Order, OrderItem, Product
from .forms import ProductEdit, ChoiceProduct


def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
        'title': 'All clients'
    }
    return render(request, "app_hw2/clients.html", context)


def client(request, client_id: int):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    order_items = {}
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order.pk] = []
        for item in items:
            order_items[order.pk].append(item)
    context = {
        'client': client,
        'orders': orders,
        'order_items': order_items,
        'title': f'Orders by {client.str_to_title()}'
    }
    return render(request, "app_hw2/client.html", context)


def client_7days(request, client_id: int):
    client = Client.objects.get(pk=client_id)
    current_date = datetime.now()
    start_date = current_date - timedelta(days=7)
    orders = Order.objects.filter(
        client=client, date_created__gte=start_date
        ).order_by('-date_created')
    order_items = {}
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order.pk] = []
        for item in items:
            order_items[order.pk].append(item)
    context = {
        'client': client,
        'orders': orders,
        'order_items': order_items,
        'title': f'Orders by {client.str_to_title()} for last 7 days'
    }
    return render(request, "app_hw2/client_orders.html", context)


def client_30days(request, client_id: int):
    client = Client.objects.get(pk=client_id)
    current_date = datetime.now()
    start_date = current_date - timedelta(days=30)
    orders = Order.objects.filter(
        client=client, date_created__gte=start_date
        ).order_by('-date_created')
    order_items = {}
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order.pk] = []
        for item in items:
            order_items[order.pk].append(item)
    context = {
        'client': client,
        'orders': orders,
        'order_items': order_items,
        'title': f'Orders by {client.str_to_title()} for last 30 days'
    }
    return render(request, "app_hw2/client_orders.html", context)



def client_365days(request, client_id: int):
    client = Client.objects.get(pk=client_id)
    current_date = datetime.now()
    start_date = current_date - timedelta(days=365)
    orders = Order.objects.filter(
        client=client, date_created__gte=start_date
        ).order_by('-date_created')
    order_items = {}
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order.pk] = []
        for item in items:
            order_items[order.pk].append(item)
    context = {
        'client': client,
        'orders': orders,
        'order_items': order_items,
        'title': f'Orders by {client.str_to_title()} for last 365 days'
    }
    return render(request, "app_hw2/client_orders.html", context)


def choice_prod(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'All products'
    }
    return render(request, "app_hw2/choice_prod.html", context)

def prod_edit(request, product_id: int):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductEdit(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return choice_prod(request)
    else:
        form = ProductEdit(instance=product)
    context = {
        'form': form,
        'product': product,
        'title': 'Edit product'
    }
    return render(request, 'app_hw2/prod_edit.html', context)