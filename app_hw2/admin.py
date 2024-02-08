from django.contrib import admin
from django.shortcuts import redirect
from .models import Client, Product, Order, OrderItem
from django.utils.html import format_html
from .views import order_create


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'register_date']
    list_display_links = ['name']
    search_fields = ["email", "name", 'address']
    list_filter = ['register_date']
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name"],
            },
        ),
        (
            "Contacts",
            {
                "classes": ["collapse"],
                "description": "Contacts",
                "fields": ['email', 'phone', 'address',],
            },
        ),
        (
            "Register Date",
            {
                "classes": ["collapse"],
                "description": "Register Date",
                "fields": ['register_date'],
            },
        ),
    ]



@admin.action(description="Reset the quantity to zero")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'added_date', 'photo_preview']
    ordering = ['pk']
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name", "description"],
            },
        ),
        (
            "Buhgaltery",
            {
                "classes": ["wide"],
                "description": "Price and Count",
                "fields": ["price", 'quantity'],
            },
        ),
        (
            "Date",
            {
                "classes": ["collapse"],
                "description": "Date Added",
                "fields": ["added_date"],
            },
        ),
        (
            "Image",
            {
                "classes": ["collapse"],
                "description": "Photo of Product",
                "fields": ["photo_preview", 'photo'],
            },
        ),
    ]
    readonly_fields = ['photo_preview']



    def photo_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="50">')
        return 'No image'




class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','client', 'total_price')
    fields = ('client', 'total_price')

    def add_view(self, request, form_url='', extra_context=None):
        return order_create(request)



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    list_filter = ['order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)