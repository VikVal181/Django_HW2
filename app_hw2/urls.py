from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.clients, name="clients"),
    path("client/<int:client_id>/", views.client, name="client"),
    path("client/<int:client_id>/order7", views.client_7days, name="client_7days"),
    path("client/<int:client_id>/order30", views.client_30days, name="client_30days"),
    path("client/<int:client_id>/order365", views.client_365days, name="client_365days"),
    path("prod_edit/<int:product_id>", views.prod_edit, name="prod_edit"),
    path("choice_prod/", views.choice_prod, name="choice_prod"),
]