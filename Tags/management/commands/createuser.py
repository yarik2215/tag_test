from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create user'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs=1, type=str)
        parser.add_argument('--pass', nargs=1, type=str)

    def handle(self, *args, **options):
        username = options.get('username')[0]
        password = options.get('pass')[0]
        user = User.objects.create_user(username=username,
                                 email='some@mail.com',
                                 password=password)
        print(f'Created user {username}, pass: {password}')
