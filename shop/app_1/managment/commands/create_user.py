from django.core.management.base import BaseCommand
from shop.app_1.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(5):
            user = User(
                name=f'user_{i}',
                email=f'user_{i}@mail.ru',
                phone_number=f'12345678{i}',
                address=f'Lenin street, {i}'
            )

            user.save()
            self.stdout.write(f'{user}')