from django.core.management.base import BaseCommand, CommandParser

from app_hw2.models import Client, Product, Order

PASSWORD = '0000'

class Command(BaseCommand):
    help = 'Delete all clients, products and orders'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **kwargs):
        if kwargs['password'] == PASSWORD:
            clients = Client.objects.all()
            products = Product.objects.all()
            orders = Order.objects.all()
            for item in clients:
                item.delete()
            for item in products:
                item.delete()
            for item in orders:
                item.delete()

            self.stdout.write('Database cleared')