from django.core.management import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    help = 'show user command'

    def handle(self, *args, **options):
        print(f"TOTAL USERS: {User.objects.all().count()}")
