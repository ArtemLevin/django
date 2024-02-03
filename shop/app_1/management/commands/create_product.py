from django.core.management.base import BaseCommand
from app_1.models import Product
from random import choice

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(5):
            product = Product(
                name=f'product_{i}',
                price = choice([i for i in range(100)]),
                description=f'description_{i}',
            )

            product.save()
            self.stdout.write(f'{product}')