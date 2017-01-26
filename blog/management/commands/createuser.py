from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--username')
        parser.add_argument('--password')
        parser.add_argument('--email', default=None)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
