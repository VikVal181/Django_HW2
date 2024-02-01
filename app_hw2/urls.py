from django.urls import path

import app_hw2.views as views

urlpatterns = [

    path('clients', views.clients_view, name='clients'),
    path('products', views.products_view, name='products'),
    path('orders', views.orders_view, name='orders'),
    path('client_orders/<int:cliennt_id>/<int:filter_days>', views.client_orders_view, name='client_orders')
]