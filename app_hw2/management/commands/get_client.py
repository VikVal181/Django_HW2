from django.core.management.base import BaseCommand
from app_hw2.models import Client


class Command(BaseCommand):
    help = 'Return client by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        result = Client.objects.filter(pk=pk).first()
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f"Client with id = {pk} doesn't exists")