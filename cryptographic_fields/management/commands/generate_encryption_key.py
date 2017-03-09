from django.core.management.base import BaseCommand

import cryptography.fernet


class Command(BaseCommand):
    help = 'Generates a new Fernet encryption key'

    def handle(self, *args, **options):
        key = cryptography.fernet.Fernet.generate_key()
        # SAS - how to properly do for both Python 2 and Python 3
        self.stdout.write(key, ending=b'\n')
