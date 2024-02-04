from django.core.management.base import BaseCommand, CommandParser
from app_hw2.models import Client, Product, Order, OrderItem
import random



class Command(BaseCommand):
    help = 'Added random order'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Count clients')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            client = random.choice(Client.objects.all())
            products_list = []
            total_price = 0
            order = Order.objects.create(client=client, total_price=total_price)
            for i in range(3):
                count_products = random.randint(1, 5)
                product = random.choice(Product.objects.all())
                if product not in products_list:
                    products_list.append(product)
                    order_item = OrderItem.objects.create(
                        order=order, 
                        product=product,
                        count=count_products,
                        price=product.price
                        )
                    order_item.save()
                    total_price += product.price * count_products
                else:
                    i -= 1
            order.total_price = total_price
            order.save()
        self.stdout.write(f"{count} orders added")