from django.core.management.base import BaseCommand, CommandParser
from app_hw2.models import Client, Product, Order
from random import randint



class Command(BaseCommand):
    help = 'Added random order'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("client_id", type=int, help='User ID')
        parser.add_argument('product_id', type=int, help='Id of product')
    

    def handle(self, *args, **options) -> None:
        client_id = options['client_id']
        product_id = options['product_id']

        client = Client.objects.get(id=client_id)
        product = Product.objects.get(id=product_id)

        order = Order (
            client = client,
            products = product,
            total_price = product.price * randint(1,5))
        order.save()
        self.stdout.write(self.style.SUCCESS(f'New orders have been added: {order}'))