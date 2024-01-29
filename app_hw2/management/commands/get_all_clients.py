from django.core.management.base import BaseCommand

from app_hw2.models import Client

class Command(BaseCommand):
    help = 'Return all clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'{client}\n')