from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order
from datetime import timedelta
from datetime import datetime as dt, timedelta

 # Create your views here.
def clients_view(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'app_hw2/clients.html', context=context)


def products_view(request):
    products = Product.objects.all()
    res_str = '<br>'.join([str(product) for product in products])
    return HttpResponse(res_str)

def orders_view(request):
    orders = Order.objects.all()
    res_str = '<br>'.join([str(order) for order in orders])
    return HttpResponse(res_str)

def client_orders_view(request, client_id: int,filter_days: int):
    products = []
    user = Client.objects.filter(pk=client_id).first()
    
    date_low_lim = (dt.now() - timedelta(filter_days))
    orders = Order.objects.filter(client=user).filter(order_date__gt=date_low_lim).order_by('order_date')
    context ={
        'user': user, 
        'orders': orders, 
        'products': products
    }
    for order in orders:
        products.append(order.products.name)
        print(order.date_created)
        print(products)
        print(order.products.name)

    return render(request, 'app_hw2/client_orders.html', context=context)