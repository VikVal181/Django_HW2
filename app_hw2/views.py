from django.shortcuts import render, redirect
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


# def choice_prod(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#         'title': 'All products'
#     }
#     return render(request, "app_hw2/choice_prod.html", context)

def prod_edit(request):
    selected_product = None
    if request.method == "POST":
        form_select = ChoiceProduct(request.POST)
        form_edit = ProductEdit(instance=selected_product)
        print(0)
        if form_select.is_valid():
            print(1)
            selected_product = form_select.cleaned_data["product"]
            form_edit = ProductEdit(
                request.POST, request.FILES, instance=selected_product
            )
            if form_edit.is_valid():
                print(2)
                form_edit.save(commit=True)
                selected_product = None
            else:
                form_edit = ProductEdit(instance=selected_product)
    else:
        form_select = ChoiceProduct()
        form_edit = ProductEdit(instance=selected_product)

    context = {
        "form_select": form_select,
        "form_edit": form_edit,
        "selected_product": selected_product,
        "title": "Edit product",
    }
    return render(request, "app_hw2/prod_edit.html", context)

def order_create(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        products = request.POST.getlist('products')
        quantities = request.POST.getlist('quantities')

        # Создаем новый заказ
        order = Order.objects.create(client_id=client_id)

        # Добавляем товары в заказ
        for product, quantity in zip(products, quantities):
            product = Product.objects.get(id=product)
            quantity = int(quantity)
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price*quantity)

        # Обновляем общую стоимость заказа
        order.total_price = sum([item.price for item in order.orderitem_set.all()])
        order.save()
        return redirect('/admin/app_hw2/order')


    clients = Client.objects.all()
    products = Product.objects.all()
    context = {'clients': clients, 'products': products}
    return render(request, 'app_hw2/order_create.html', context)